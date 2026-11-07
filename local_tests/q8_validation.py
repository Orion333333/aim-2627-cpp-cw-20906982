"""Compare Q8 with stable grouping and batch-transformation checks."""

import hashlib
import json
import random
import shutil
import subprocess
import tempfile
from itertools import groupby
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_q8.cpp'
SEED = 2627
RANDOM_CASES = 1000
MODES = ('mixed', 'field_edges', 'dense_duplicates', 'invalid_then_valid',
         'valid_then_invalid', 'negative_hp', 'unique_ids', 'all_invalid')
DRIVER = r'''#define main q8_public_main
#include "@SOURCE@"
#undef main

void check_unchanged(const std::vector<aim::q8::Telemetry>& frames,
                     const std::vector<aim::q8::Telemetry>& saved)
{
  CHECK(frames.size() == saved.size());
  for (std::size_t i = 0; i < frames.size(); ++i) {
    CHECK(frames[i].id == saved[i].id && frames[i].hp == saved[i].hp);
  }
}

void print_result(const aim::q8::Summary& result)
{
  std::cout << result.valid << ' ' << result.duplicate << ' ' << result.invalid
            << ' ' << result.total_hp << ' ' << result.ids.size();
  for (int id : result.ids) {
    std::cout << ' ' << id;
  }
  std::cout << '\n';
}

int main()
{
  try {
    int count;
    std::cin >> count;
    for (int i = 0; i < count; ++i) {
      int n;
      std::cin >> n;
      std::vector<aim::q8::Telemetry> frames(n);
      for (auto& frame : frames) {
        std::cin >> frame.id >> frame.hp;
      }
      const auto saved = frames;
      auto full = aim::q8::summarize(frames);
      check_unchanged(frames, saved);
      print_result(full);

      auto reversed = saved;
      std::reverse(reversed.begin(), reversed.end());
      const auto savedReversed = reversed;
      print_result(aim::q8::summarize(reversed));
      check_unchanged(reversed, savedReversed);

      auto doubled = saved;
      doubled.insert(doubled.end(), saved.begin(), saved.end());
      const auto savedDoubled = doubled;
      auto repeated = aim::q8::summarize(doubled);
      check_unchanged(doubled, savedDoubled);
      CHECK(repeated.valid == full.valid);
      CHECK(repeated.duplicate == 2 * full.duplicate + full.valid);
      CHECK(repeated.invalid == 2 * full.invalid);
      CHECK(repeated.total_hp == full.total_hp && repeated.ids == full.ids);
      print_result(repeated);

      std::vector<aim::q8::Telemetry> empty;
      auto reset = aim::q8::summarize(empty);
      CHECK(empty.empty());
      CHECK(reset.valid == 0 && reset.duplicate == 0 && reset.invalid == 0);
      CHECK(reset.total_hp == 0 && reset.ids.empty());
      print_result(reset);
    }
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
'''


def reference(frames):
    legal = [(identifier, hp) for identifier, hp in frames
             if 0 <= identifier <= 9999 and -1000 <= hp <= 1000]
    ordered = sorted(legal, key=lambda item: item[0])
    identifiers = []
    contributions = []
    for identifier, group in groupby(ordered, key=lambda item: item[0]):
        identifiers.append(identifier)
        first_hp = next(group)[1]
        contributions.append(min(100, max(0, first_hp)))
    valid = len(identifiers)
    return [valid, len(legal) - valid, len(frames) - len(legal),
            sum(contributions), identifiers]


def make_cases():
    rng = random.Random(SEED)
    id_edges = [-(2 ** 31), -1, 0, 1, 9998, 9999, 10000, 2 ** 31 - 1]
    hp_edges = [-(2 ** 31), -1001, -1000, -1, 0, 1, 99, 100, 101,
                1000, 1001, 2 ** 31 - 1]
    cases = []
    for index in range(RANDOM_CASES):
        mode = index % len(MODES)
        n = 10000 if index % 101 == 0 else rng.randrange(151)
        frames = [(rng.randint(-100, 10100), rng.randint(-1100, 1100))
                  for _ in range(n)]
        if mode == 1:
            frames = [(rng.choice(id_edges), rng.choice(hp_edges))
                      for _ in range(n)]
        elif mode == 2:
            frames = [(rng.randrange(16), rng.randint(-1000, 1000))
                      for _ in range(n)]
        elif mode == 3:
            frames = []
            for identifier in rng.sample(range(10000), (n + 2) // 3):
                frames.extend([(identifier, rng.choice([-1001, 1001])),
                               (identifier, rng.randint(-1000, 1000)),
                               (identifier, rng.randint(-1000, 1000))])
            frames = frames[:n]
        elif mode == 4:
            frames = []
            for identifier in rng.sample(range(10000), (n + 1) // 2):
                frames.extend([(identifier, rng.randint(-1000, 1000)),
                               (identifier, rng.choice([-1001, 1001,
                                                        -(2 ** 31)]))])
            frames = frames[:n]
        elif mode == 5:
            frames = [(rng.randrange(64), rng.randint(-1000, 0))
                      for _ in range(n)]
        elif mode == 6:
            identifiers = sorted(rng.sample(range(10000), n), reverse=True)
            frames = [(identifier, rng.randint(-1000, 1000))
                      for identifier in identifiers]
        elif mode == 7:
            frames = [(rng.choice([-1, 10000, -(2 ** 31), 2 ** 31 - 1]),
                       rng.choice(hp_edges)) if position % 2 == 0 else
                      (rng.randrange(10000), rng.choice([-1001, 1001,
                                                        -(2 ** 31)]))
                      for position in range(n)]
        cases.append(frames)
    return cases


def flatten(result):
    return result[:4] + [len(result[4]), *result[4]]


def main():
    cases = make_cases()
    expected = []
    payload = [str(len(cases))]
    reversed_total_changes = 0
    for frames in cases:
        full = reference(frames)
        reversed_result = reference(list(reversed(frames)))
        reversed_total_changes += full[3] != reversed_result[3]
        valid, duplicate, invalid, total_hp, identifiers = full
        repeated = [valid, 2 * duplicate + valid, 2 * invalid,
                    total_hp, identifiers]
        assert reference(frames + frames) == repeated
        expected.extend(map(flatten, [full, reversed_result, repeated,
                                      [0, 0, 0, 0, []]]))
        payload.append(str(len(frames)))
        payload.extend(f'{identifier} {hp}' for identifier, hp in frames)

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='q8-validation-') as directory:
        harness = Path(directory) / 'q8_driver.cpp'
        binary = Path(directory) / 'q8_driver.exe'
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
            capture_output=True, text=True, timeout=20, check=True)
    actual = completed.stdout.splitlines()
    if len(actual) != len(expected):
        raise AssertionError('The driver returned the wrong result count')
    for index, (line, wanted) in enumerate(zip(actual, expected)):
        if list(map(int, line.split())) != wanted:
            case, variant = divmod(index, 4)
            raise AssertionError(
                f'Case {case}, variant {variant}: input={cases[case]!r}, '
                f'expected={wanted!r}, actual={line!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    max_batches = sum(len(frames) == 10000 for frames in cases)
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_cases': len(cases),
        'cpp_calls': len(expected),
        'reversed_checks': len(cases),
        'reversed_total_changes': reversed_total_changes,
        'doubled_batch_checks': len(cases),
        'empty_reset_checks': len(cases),
        'input_unchanged_checks': len(expected),
        'max_length_doubled_batches': max_batches,
        'modes': {mode: RANDOM_CASES // len(MODES) for mode in MODES},
        'reference': 'stable sort of legal records, then group by ID',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/q8-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'Q8 validation passed: {len(cases)} random cases, '
          f'{len(expected)} calls, {len(cases)} doubled-batch checks, '
          f'{len(cases)} empty resets ({max_batches} batches with '
          f'20000 records, seed {SEED})')


if __name__ == '__main__':
    main()
