"""Compare Q6 with an independent Python filter-and-sort reference."""

import hashlib
import json
import random
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_q6.cpp'
SEED = 2627
RANDOM_CASES = 1000
MODES = ('wide', 'hp_priority', 'distance_priority', 'id_ties',
         'range_edge', 'negative_range', 'zero_range', 'no_candidate')


def reference(targets, max_range):
    if max_range < 0:
        return -1
    candidates = [(hp, x * x + y * y, identifier)
                  for identifier, x, y, hp, visible in targets
                  if visible and hp > 0 and x * x + y * y <= max_range ** 2]
    candidates.sort()
    return candidates[0][2] if candidates else -1


def make_cases():
    rng = random.Random(SEED)
    cases = []
    for index in range(RANDOM_CASES):
        mode = index % len(MODES)
        count = rng.randint(3, 120) if mode in (
            1, 2, 3, 4) else rng.randrange(121)
        identifiers = rng.sample(range(1, 2 ** 31 - 1), count)
        if count and index % 2 == 0:
            identifiers[0] = 0
        if count > 1 and index % 3 == 0:
            identifiers[-1] = 2 ** 31 - 1
        targets = [(identifier, rng.randint(-10 ** 6, 10 ** 6),
                    rng.randint(-10 ** 6, 10 ** 6), rng.randint(-100, 100),
                    bool(rng.randrange(2))) for identifier in identifiers]
        max_range = rng.choice([0, 1, 5, 50000, 10 ** 6,
                                rng.randrange(10 ** 6 + 1)])
        if mode in (1, 2):
            common_hp = rng.randint(1, 100)
            targets = [(identifier, rng.randint(-10, 10), rng.randint(-10, 10),
                        rng.randint(1, 100) if mode == 1 else common_hp, True)
                       for identifier in identifiers]
            max_range = 20
        elif mode == 3:
            scale = rng.randint(1, 200000)
            hp = rng.randint(1, 100)
            points = [(3, 4), (-3, 4), (3, -4), (-3, -4), (0, 5), (5, 0)]
            targets = []
            for identifier in identifiers:
                x, y = rng.choice(points)
                targets.append((identifier, x * scale, y * scale, hp, True))
            max_range = 5 * scale
        elif mode == 4:
            scale = rng.choice([1, 10000, 200000, rng.randint(1, 200000)])
            max_range = 5 * scale
            targets = [(identifier, max_range, 1, 1, True)
                       for identifier in identifiers]
            targets[0] = (identifiers[0], -3 * scale, 4 * scale, 1, True)
            targets[-1] = (identifiers[-1], 0, 0, 2, True)
        elif mode == 5:
            max_range = rng.choice([-1, -10, -(2 ** 31)])
        elif mode == 6:
            max_range = 0
            targets = [(identifier, rng.randint(-1, 1), rng.randint(-1, 1),
                        rng.choice([-100, 0, 1, 100]), bool(rng.randrange(2)))
                       for identifier in identifiers]
        elif mode == 7:
            max_range = 10 ** 6
            targets = []
            for position, identifier in enumerate(identifiers):
                if position % 3 == 0:
                    targets.append((identifier, 0, 0, 1, False))
                elif position % 3 == 1:
                    targets.append(
                        (identifier, 0, 0, rng.randint(-100, 0), True))
                else:
                    targets.append((identifier, 10 ** 6, -10 ** 6, 1, True))
        cases.append((targets, max_range))
    return cases


def main():
    cases = make_cases()
    rng = random.Random(SEED + 1)
    expected = []
    payload = [str(3 * len(cases))]
    winners = 0
    for targets, max_range in cases:
        wanted = reference(targets, max_range)
        winners += wanted != -1
        shuffled = list(targets)
        rng.shuffle(shuffled)
        for variant in (targets, list(reversed(targets)), shuffled):
            expected.append(wanted)
            payload.append(f'{len(variant)} {max_range}')
            payload.extend(f'{identifier} {x} {y} {hp} {int(visible)}'
                           for identifier, x, y, hp, visible in variant)

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='q6-validation-') as directory:
        harness = Path(directory) / 'q6_driver.cpp'
        binary = Path(directory) / 'q6_driver.exe'
        harness.write_text(
            '#define main q6_public_main\n'
            f'#include "{SOURCE.as_posix()}"\n'
            '#undef main\n'
            'int main()\n'
            '{\n'
            '  try {\n'
            '    int count;\n'
            '    std::cin >> count;\n'
            '    for (int i = 0; i < count; ++i) {\n'
            '      int n, range;\n'
            '      std::cin >> n >> range;\n'
            '      std::vector<aim::q6::Target> targets(n);\n'
            '      for (auto& target : targets) {\n'
            '        std::cin >> target.id >> target.x >> target.y\n'
            '                 >> target.hp >> target.visible;\n'
            '      }\n'
            '      const auto saved = targets;\n'
            '      int result = aim::q6::select_target(targets, range);\n'
            '      CHECK(targets.size() == saved.size());\n'
            '      for (std::size_t j = 0; j < targets.size(); ++j) {\n'
            '        CHECK(targets[j].id == saved[j].id &&\n'
            '              targets[j].x == saved[j].x &&\n'
            '              targets[j].y == saved[j].y &&\n'
            '              targets[j].hp == saved[j].hp &&\n'
            '              targets[j].visible == saved[j].visible);\n'
            '      }\n'
            "      std::cout << result << '\\n';\n"
            '    }\n'
            '  } catch (const std::exception& error) {\n'
            "    std::cerr << error.what() << '\\n';\n"
            '    return 1;\n'
            '  }\n'
            '  return 0;\n'
            '}\n', encoding='utf-8')
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
        if line != str(wanted):
            case, variant = divmod(index, 3)
            raise AssertionError(
                f'Case {case}, variant {variant}: input={cases[case]!r}, '
                f'expected={wanted}, actual={line!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_cases': len(cases),
        'cpp_calls': len(expected),
        'permutation_checks': 2 * len(cases),
        'input_unchanged_checks': len(expected),
        'with_candidate': winners,
        'without_candidate': len(cases) - winners,
        'modes': {mode: RANDOM_CASES // len(MODES) for mode in MODES},
        'reference': 'Python arbitrary-precision filter and tuple sort',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/q6-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'Q6 validation passed: {len(cases)} random cases, '
          f'{len(expected)} calls, {2 * len(cases)} permutation checks '
          f'(seed {SEED})')


if __name__ == '__main__':
    main()
