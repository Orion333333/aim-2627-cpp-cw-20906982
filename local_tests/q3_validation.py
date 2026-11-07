"""Compare Q3 with independently recomputed Python window sums."""

import hashlib
import json
import random
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_q3.cpp'
SEED = 2627
RANDOM_CASES = 1000


def reference(values, k, threshold):
    if k < 1 or k > len(values):
        return []
    return [right for right in range(k - 1, len(values))
            if sum(values[right - k + 1:right + 1]) > threshold]


def make_cases():
    rng = random.Random(SEED)
    pool = [-1000000000, -10, -1, 0, 1, 10, 1000000000]
    cases = []
    for _ in range(RANDOM_CASES):
        n = rng.randrange(101)
        values = rng.choices(pool, k=n)
        if n and rng.randrange(5):
            k = rng.randint(1, n)
        else:
            k = rng.choice([-1, 0, n + 1, -(2 ** 31), 2 ** 31 - 1])
        threshold = rng.choice([-10 ** 15, 10 ** 15, -1, 0, 1])
        if 1 <= k <= n and rng.randrange(4):
            left = rng.randrange(n - k + 1)
            threshold = sum(values[left:left + k]) + rng.choice([-1, 0, 1])
        cases.append((values, k, threshold))
    return cases


def main():
    cases = make_cases()
    expected = [reference(*case) for case in cases]
    lines = [str(len(cases))]
    for values, k, threshold in cases:
        lines.append(f'{len(values)} {k} {threshold}')
        lines.append(' '.join(map(str, values)))

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='q3-validation-') as directory:
        harness = Path(directory) / 'q3_driver.cpp'
        binary = Path(directory) / 'q3_driver.exe'
        harness.write_text(
            '#define main q3_public_main\n'
            f'#include "{SOURCE.as_posix()}"\n'
            '#undef main\n'
            'int main()\n'
            '{\n'
            '  int count;\n'
            '  std::cin >> count;\n'
            '  for (int i = 0; i < count; ++i) {\n'
            '    int n, k;\n'
            '    long long threshold;\n'
            '    std::cin >> n >> k >> threshold;\n'
            '    std::vector<int> values(n);\n'
            '    for (int& value : values) {\n'
            '      std::cin >> value;\n'
            '    }\n'
            '    auto result = aim::q3::alarms(values, k, threshold);\n'
            '    std::cout << result.size();\n'
            '    for (int index : result) {\n'
            "      std::cout << ' ' << index;\n"
            '    }\n'
            "    std::cout << '\\n';\n"
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
            [str(binary)], input='\n'.join(lines) + '\n',
            capture_output=True, text=True, timeout=15, check=True)
    output_lines = completed.stdout.splitlines()
    if len(output_lines) != len(expected):
        raise AssertionError('The driver returned the wrong result count')
    for index, (line, wanted) in enumerate(zip(output_lines, expected)):
        fields = list(map(int, line.split()))
        if not fields or fields[0] != len(fields) - 1:
            raise AssertionError(f'Malformed output for case {index}: {line}')
        if fields[1:] != wanted:
            raise AssertionError(
                f'Case {index}: input={cases[index]!r}, '
                f'expected={wanted!r}, actual={fields[1:]!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_cases': RANDOM_CASES,
        'reference': 'independent Python sum for every complete window',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/q3-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'Q3 validation passed: {RANDOM_CASES} random cases (seed {SEED})')


if __name__ == '__main__':
    main()
