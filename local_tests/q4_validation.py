"""Compare Q4 with an independent regular-expression transaction model."""

import hashlib
import json
import random
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_q4.cpp'
SEED = 2627
RANDOM_CASES = 1000
WHITESPACE = ' \t\n\r\v\f'
COMMAND = re.compile(r'(ADD|SET)[ \t\n\r\v\f]+([+-]?[0-9]+)')


def reference(lines):
    value = accepted = rejected = 0
    for line in lines:
        text = line.strip(WHITESPACE)
        if text == 'RESET':
            candidate = 0
        else:
            match = COMMAND.fullmatch(text)
            if not match:
                rejected += 1
                continue
            operation, number = match.groups()
            digits = number.lstrip('+-').lstrip('0') or '0'
            if len(digits) > 7:
                rejected += 1
                continue
            operand = int(digits) * (-1 if number.startswith('-') else 1)
            if not -1000000 <= operand <= 1000000:
                rejected += 1
                continue
            candidate = value + operand if operation == 'ADD' else operand
        if -1000000 <= candidate <= 1000000:
            value = candidate
            accepted += 1
        else:
            rejected += 1
    return [value, accepted, rejected]


def make_cases():
    rng = random.Random(SEED)
    samples = [
        '', ' ', 'ADD', 'SET', 'RESET x', 'add 1', 'MUL 2',
        'ADD 1.0', 'SET 2x', 'SET 0x10', 'ADD +', 'ADD +-2',
        'SET + 1', 'ADD 1000001', 'SET -1000001', 'ADD+2', 'SET 1e3',
        'ADD 9223372036854775808', 'SET -9223372036854775809',
        'SET +' + '0' * 1000 + '1', 'ADD ' + '9' * 1000,
        'ADD\t+0002', 'RESET\r\n', ' \tSET -1000000\v', 'ADD 1\0',
    ]
    padding = ['', ' ', '\t', '\r', '\n', '\v', '\f', ' \t']
    cases = []
    for _ in range(RANDOM_CASES):
        lines = []
        for _ in range(rng.randrange(101)):
            if rng.randrange(2):
                line = rng.choice(samples)
            else:
                operation = rng.choice(['ADD', 'SET', 'RESET'])
                if operation == 'RESET':
                    line = operation
                else:
                    value = rng.choice([-1000000, -999999, -1, 0, 1,
                                        999999, 1000000])
                    zeros = ('-' if value < 0 else '+') + '000'
                    number = rng.choice([str(value), f'{value:+d}',
                                         zeros + str(abs(value))])
                    line = operation + rng.choice([' ', '\t', '\n', '\v'])
                    line += number
                line = rng.choice(padding) + line + rng.choice(padding)
            lines.append(line)
        cases.append(lines)
    return cases


def main():
    cases = make_cases()
    expected = [reference(lines) for lines in cases]
    payload = [str(len(cases))]
    for lines in cases:
        payload.append(str(len(lines)))
        payload.extend(line.encode('utf-8').hex() or '-' for line in lines)

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='q4-validation-') as directory:
        harness = Path(directory) / 'q4_driver.cpp'
        binary = Path(directory) / 'q4_driver.exe'
        harness.write_text(
            '#define main q4_public_main\n'
            f'#include "{SOURCE.as_posix()}"\n'
            '#undef main\n'
            'int main()\n'
            '{\n'
            '  int count;\n'
            '  std::cin >> count;\n'
            '  for (int i = 0; i < count; ++i) {\n'
            '    int lineCount;\n'
            '    std::cin >> lineCount;\n'
            '    std::vector<std::string> lines;\n'
            '    for (int j = 0; j < lineCount; ++j) {\n'
            '      std::string encoded, line;\n'
            '      std::cin >> encoded;\n'
            '      if (encoded != "-") {\n'
            '        for (std::size_t k = 0; k < encoded.size(); k += 2) {\n'
            '          int byte = std::stoi(encoded.substr(k, 2),\n'
            '                               nullptr, 16);\n'
            '          line += static_cast<char>(byte);\n'
            '        }\n'
            '      }\n'
            '      lines.push_back(line);\n'
            '    }\n'
            '    auto result = aim::q4::execute(lines);\n'
            "    std::cout << result.value << ' ' << result.accepted\n"
            "              << ' ' << result.rejected << '\\n';\n"
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
        result = list(map(int, line.split()))
        if result != wanted:
            raise AssertionError(
                f'Case {index}: expected={wanted!r}, actual={result!r}, '
                f'input={cases[index]!r}')
        assert result[1] + result[2] == len(cases[index])
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_sequences': RANDOM_CASES,
        'reference': 'full-match regex and independent integer state updates',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/q4-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'Q4 validation passed: {RANDOM_CASES} random sequences '
          f'(seed {SEED})')


if __name__ == '__main__':
    main()
