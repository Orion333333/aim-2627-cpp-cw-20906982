"""Compare Q7 with an event-based cooling model and split-run checks."""

import hashlib
import json
import random
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_q7.cpp'
SEED = 2627
RANDOM_CASES = 1000
MODES = ('mixed', 'parameter_edges', 'idle_or_empty', 'no_ammo',
         'no_cooling', 'no_shot_heat', 'heat_limit', 'sparse_requests')
DRIVER = r'''#define main q7_public_main
#include "@SOURCE@"
#undef main

void print_result(const aim::q7::FireResult& result)
{
  std::cout << result.shots << ' ' << result.rejected << ' '
            << result.ammo << ' ' << result.heat;
}

int main()
{
  try {
    int count;
    std::cin >> count;
    for (int i = 0; i < count; ++i) {
      int n, ammo, heat, cool, shotHeat, split;
      std::cin >> n >> ammo >> heat >> cool >> shotHeat >> split;
      std::vector<int> requests(n);
      for (int& request : requests) {
        std::cin >> request;
      }
      const auto saved = requests;
      auto full = aim::q7::simulate(ammo, heat, cool, shotHeat, requests);
      CHECK(requests == saved);

      std::vector<int> first(saved.begin(), saved.begin() + split);
      const auto savedFirst = first;
      auto left = aim::q7::simulate(ammo, heat, cool, shotHeat, first);
      CHECK(first == savedFirst);

      std::vector<int> second(saved.begin() + split, saved.end());
      const auto savedSecond = second;
      auto right = aim::q7::simulate(left.ammo, left.heat, cool, shotHeat, second);
      CHECK(second == savedSecond);
      CHECK(full.shots == left.shots + right.shots);
      CHECK(full.rejected == left.rejected + right.rejected);
      CHECK(full.ammo == right.ammo && full.heat == right.heat);

      print_result(full);
      std::cout << ' ';
      print_result(left);
      std::cout << ' ';
      print_result(right);
      std::cout << '\n';
    }
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
'''


def reference(ammo, heat, cool, shot_heat, requests):
    fired = []
    previous_request = -1
    for frame, request in enumerate(requests):
        if request == 0:
            continue
        heat = max(0, heat - cool * (frame - previous_request))
        if len(fired) < ammo and heat <= 100 - shot_heat:
            fired.append(frame)
            heat += shot_heat
        previous_request = frame
    heat = max(0, heat - cool * (len(requests) - 1 - previous_request))
    return [len(fired), sum(requests) - len(fired), ammo - len(fired), heat]


def make_cases():
    rng = random.Random(SEED)
    cases = []
    for index in range(RANDOM_CASES):
        mode = index % len(MODES)
        n = 10000 if index % 101 == 0 else rng.randrange(201)
        ammo, heat, cool, shot_heat = [rng.randrange(101) for _ in range(4)]
        requests = [rng.randrange(2) for _ in range(n)]
        if mode == 1:
            ammo, heat, cool, shot_heat = [rng.choice([0, 1, 99, 100])
                                           for _ in range(4)]
        elif mode == 2:
            requests = [] if (index // len(MODES)) % 2 == 0 else [0] * n
        elif mode == 3:
            ammo = 0
        elif mode == 4:
            cool = 0
            heat = rng.choice([0, 50, 99, 100])
            shot_heat = rng.choice([1, 50, 100])
        elif mode == 5:
            shot_heat = 0
        elif mode == 6:
            ammo = rng.randint(1, 100)
            cool = rng.choice([0, 1, 10, 100])
            heat = min(100, max(0, 100 - shot_heat + cool
                                + rng.choice([-1, 0, 1])))
            if requests:
                requests[0] = 1
        elif mode == 7:
            heat = shot_heat = 100
            cool = rng.choice([0, 1, 2, 10, 100])
            requests = [int(rng.randrange(10) == 0) for _ in range(n)]
            if requests:
                requests[-1] = 1
        split = rng.choice(
            [0, len(requests), rng.randrange(len(requests) + 1)])
        cases.append((ammo, heat, cool, shot_heat, requests, split))
    return cases


def main():
    cases = make_cases()
    expected = []
    payload = [str(len(cases))]
    for ammo, heat, cool, shot_heat, requests, split in cases:
        full = reference(ammo, heat, cool, shot_heat, requests)
        left = reference(ammo, heat, cool, shot_heat, requests[:split])
        right = reference(left[2], left[3], cool, shot_heat, requests[split:])
        assert full == [left[0] + right[0], left[1] + right[1], *right[2:]]
        expected.append(full + left + right)
        payload.append(f'{len(requests)} {ammo} {heat} {
                       cool} {shot_heat} {split}')
        payload.append(' '.join(map(str, requests)))

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='q7-validation-') as directory:
        harness = Path(directory) / 'q7_driver.cpp'
        binary = Path(directory) / 'q7_driver.exe'
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
            capture_output=True, text=True, timeout=15, check=True)
    actual = completed.stdout.splitlines()
    if len(actual) != len(expected):
        raise AssertionError('The driver returned the wrong result count')
    for index, (line, wanted) in enumerate(zip(actual, expected)):
        if list(map(int, line.split())) != wanted:
            raise AssertionError(f'Case {index}: input={cases[index]!r}, '
                                 f'expected={wanted!r}, actual={line!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    long_cases = sum(len(case[4]) == 10000 for case in cases)
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_cases': len(cases),
        'cpp_calls': 3 * len(cases),
        'continuation_checks': len(cases),
        'input_unchanged_checks': 3 * len(cases),
        'max_length_cases': long_cases,
        'modes': {mode: RANDOM_CASES // len(MODES) for mode in MODES},
        'reference': 'aggregate cooling between requests; count firing events',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/q7-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'Q7 validation passed: {len(cases)} random cases, '
          f'{3 * len(cases)} calls, {len(cases)} continuation checks '
          f'({long_cases} cases with 10000 frames, seed {SEED})')


if __name__ == '__main__':
    main()
