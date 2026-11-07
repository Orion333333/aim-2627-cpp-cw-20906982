"""Compare B2 with a stable Python filter and repeat-compaction checks."""

import hashlib
import json
import random
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_b2.cpp'
SEED = 2627
RANDOM_CASES = 1000
MIN_VALUE = -(2 ** 31)
MAX_VALUE = 2 ** 31 - 1
MODES = ('mixed', 'int_edges', 'duplicates', 'all_kept', 'all_removed',
         'equal_bounds', 'reversed_bounds', 'rejected_prefix')
DRIVER = r'''#define main b2_public_main
#include "@SOURCE@"
#undef main

void print_prefix(const int* data, std::size_t kept)
{
  std::cout << kept;
  for (std::size_t i = 0; i < kept; ++i) {
    std::cout << ' ' << data[i];
  }
  std::cout << '\n';
}

int main()
{
  try {
    int count;
    std::cin >> count;
    for (int i = 0; i < count; ++i) {
      int n, low, high;
      std::cin >> n >> low >> high;
      std::vector<int> storage(n + 2);
      storage.front() = 123456789;
      storage.back() = -987654321;
      for (int j = 0; j < n; ++j) {
        std::cin >> storage[j + 1];
      }
      const auto saved = storage;
      int* data = storage.data() + 1;
      std::size_t kept = aim::b2::compact(data, n, low, high);
      CHECK(kept <= static_cast<std::size_t>(n));
      CHECK(storage.front() == saved.front() && storage.back() == saved.back());
      if (low > high) {
        CHECK(storage == saved);
      }
      print_prefix(data, kept);

      const auto afterFirst = storage;
      std::size_t repeated = aim::b2::compact(data, kept, low, high);
      CHECK(repeated == kept);
      CHECK(storage == afterFirst);
      print_prefix(data, repeated);
    }
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
'''


def reference(values, low, high):
    if low > high:
        return []
    return [value for value in values if low <= value <= high]


def make_cases():
    rng = random.Random(SEED)
    edges = [MIN_VALUE, MIN_VALUE + 1, -1, 0, 1, MAX_VALUE - 1, MAX_VALUE]
    cases = []
    for index in range(RANDOM_CASES):
        mode = index % len(MODES)
        n = 200000 if index % 101 == 0 else rng.randrange(201)
        values = rng.choices(range(-20, 21), k=n)
        low, high = rng.randint(-25, 25), rng.randint(-25, 25)
        if mode == 1:
            values = rng.choices(edges, k=n)
            low, high = rng.choice(edges), rng.choice(edges)
        elif mode == 2:
            pool = [rng.choice(edges) for _ in range(4)]
            values = rng.choices(pool, k=n)
            low, high = sorted([rng.choice(pool), rng.choice(pool)])
        elif mode == 3:
            values = [rng.randint(MIN_VALUE, MAX_VALUE) for _ in range(n)]
            low, high = MIN_VALUE, MAX_VALUE
        elif mode == 4:
            values = rng.choices([MIN_VALUE, -1, 1, MAX_VALUE], k=n)
            low = high = 0
        elif mode == 5:
            low = high = rng.choice(edges)
            values = rng.choices([low, MIN_VALUE, MAX_VALUE, 0], k=n)
        elif mode == 6:
            low, high = rng.randint(1, 100), rng.randint(-100, 0)
        elif mode == 7:
            low, high = 0, 100
            prefix = n // 2
            values = [-1] * prefix + rng.choices(range(101), k=n - prefix)
        cases.append((values, low, high))
    return cases


def main():
    cases = make_cases()
    expected = []
    payload = [str(len(cases))]
    reversed_cases = 0
    kept_elements = 0
    for values, low, high in cases:
        wanted = reference(values, low, high)
        expected.extend([wanted, wanted])
        reversed_cases += low > high
        kept_elements += 2 * len(wanted)
        payload.append(f'{len(values)} {low} {high}')
        payload.append(' '.join(map(str, values)))

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='b2-validation-') as directory:
        harness = Path(directory) / 'b2_driver.cpp'
        binary = Path(directory) / 'b2_driver.exe'
        harness.write_text(DRIVER.replace('@SOURCE@', SOURCE.as_posix()),
                           encoding='utf-8')
        command = [compiler, '-std=c++17', '-Wall', '-Wextra', '-pedantic',
                   '-Werror', str(harness), '-o', str(binary)]
        compiled = subprocess.run(command, capture_output=True, text=True,
                                  timeout=45, check=False)
        if compiled.returncode:
            raise RuntimeError(compiled.stdout + compiled.stderr)
        completed = subprocess.run(
            [str(binary)], input='\n'.join(payload) + '\n',
            capture_output=True, text=True, timeout=40, check=True)
    actual = completed.stdout.splitlines()
    if len(actual) != len(expected):
        raise AssertionError('The driver returned the wrong result count')
    for index, (line, wanted) in enumerate(zip(actual, expected)):
        fields = list(map(int, line.split()))
        if not fields or fields[0] != len(wanted) or fields[1:] != wanted:
            case, variant = divmod(index, 2)
            raise AssertionError(
                f'Case {case}, variant {variant}: input={cases[case]!r}, '
                f'expected={wanted!r}, actual={fields!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    maximum_cases = sum(len(values) == 200000 for values, _, _ in cases)
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_cases': len(cases),
        'cpp_calls': len(expected),
        'idempotence_checks': len(cases),
        'guard_checks': len(expected),
        'reversed_range_cases': reversed_cases,
        'kept_elements_compared': kept_elements,
        'max_length_cases': maximum_cases,
        'modes': {mode: RANDOM_CASES // len(MODES) for mode in MODES},
        'reference': 'Python list filter preserving encounter order',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/b2-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'B2 validation passed: {len(cases)} random cases, '
          f'{len(expected)} calls, {len(cases)} idempotence checks '
          f'({maximum_cases} cases with 200000 elements, seed {SEED})')


if __name__ == '__main__':
    main()
