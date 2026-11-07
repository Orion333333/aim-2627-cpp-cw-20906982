"""Compare the saved Q2 implementation with an independent list-based model."""

import hashlib
import json
import random
import shutil
import subprocess
import tempfile
from pathlib import Path


SEED = 2627
RANDOM_CASES = 1000
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_q2.cpp'


def reference(labels, edits):
    tokens = labels.split(',') if labels else []
    for old, new in edits:
        if not old:
            if new:
                tokens.append(new)
        elif old in tokens:
            index = tokens.index(old)
            if new:
                tokens[index] = new
            else:
                del tokens[index]
    return ','.join(tokens)


def make_cases():
    long_label = 'a' * 32
    initial = ','.join([long_label] * 30 + ['tail123456'])
    assert len(initial) == 1000
    cases = [
        (initial, [('', 'b' * 32)] * 200),
        (initial, [(long_label, '')] * 30 + [('tail123456', '')]
         + [('', '')] * 169),
        (initial, [('tail123456', 'c' * 32),
                   ('c' * 32, 'tail123456')] * 100),
    ]
    rng = random.Random(SEED)
    vocabulary = ['a', 'aa', 'A', 'b', 'cam', 'cam2', 'webcam',
                  'cam_1', 'Cam', 'imu', 'radar', 'Z_9', 'x' * 32]
    for _ in range(RANDOM_CASES):
        labels = ','.join(rng.choices(vocabulary, k=rng.randrange(31)))
        edits = []
        for _ in range(rng.randrange(201)):
            old = '' if rng.randrange(4) == 0 else rng.choice(vocabulary)
            new = '' if rng.randrange(3) == 0 else rng.choice(vocabulary)
            edits.append((old, new))
        cases.append((labels, edits))
    return cases


def main():
    cases = make_cases()
    expected = [reference(labels, edits) for labels, edits in cases]
    assert len(expected[0]) == 7600
    assert expected[1] == ''
    assert expected[2] == cases[2][0]
    assert all(len(labels) <= 1000 and len(edits) <= 200
               for labels, edits in cases)
    lines = [str(len(cases))]
    for labels, edits in cases:
        lines.extend([labels, str(len(edits))])
        for old, new in edits:
            lines.extend([old, new])

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='q2-validation-') as directory:
        harness = Path(directory) / 'q2_driver.cpp'
        binary = Path(directory) / 'q2_driver.exe'
        harness.write_text(
            '#define main q2_public_main\n'
            f'#include "{SOURCE.as_posix()}"\n'
            '#undef main\n'
            'int main()\n'
            '{\n'
            '  std::string line;\n'
            '  std::getline(std::cin, line);\n'
            '  int count = std::stoi(line);\n'
            '  for (int i = 0; i < count; ++i) {\n'
            '    std::string labels;\n'
            '    std::getline(std::cin, labels);\n'
            '    std::getline(std::cin, line);\n'
            '    int editCount = std::stoi(line);\n'
            '    std::vector<aim::q2::LabelEdit> edits;\n'
            '    for (int j = 0; j < editCount; ++j) {\n'
            '      aim::q2::LabelEdit edit;\n'
            '      std::getline(std::cin, edit.from);\n'
            '      std::getline(std::cin, edit.to);\n'
            '      edits.push_back(edit);\n'
            '    }\n'
            '    std::cout << aim::q2::edit_labels(labels, edits)'
            " << '\\n';\n"
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
    actual = completed.stdout.splitlines()
    if len(actual) != len(expected):
        raise AssertionError('The driver returned the wrong result count')
    for index, (result, wanted) in enumerate(zip(actual, expected)):
        if result != wanted:
            raise AssertionError(
                f'Case {index}: input={cases[index]!r}, '
                f'expected={wanted!r}, actual={result!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'scale_cases': 3,
        'random_sequences': RANDOM_CASES,
        'max_initial_length': max(len(labels) for labels, _ in cases),
        'max_edits': max(len(edits) for _, edits in cases),
        'growth_case_result_length': len(actual[0]),
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/q2-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'Q2 validation passed: 3 scale cases + {RANDOM_CASES} random '
          f'sequences (seed {SEED})')


if __name__ == '__main__':
    main()
