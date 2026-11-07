"""Compare B1 with an ASCII regex and arbitrary-precision integer reference."""

import hashlib
import json
import random
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_b1.cpp'
SEED = 2627
RANDOM_CASES = 1000
MIN_VALUE = -(2 ** 31)
MAX_VALUE = 2 ** 31 - 1
GRAMMAR = re.compile(rb'[+-]?[0-9]+')
MODES = ('valid_values', 'range_edges', 'padded_values', 'overflow_values',
         'mutated_syntax', 'arbitrary_bytes', 'syntax_edges', 'digit_runs')
DRIVER = r'''#define main b1_public_main
#include "@SOURCE@"
#undef main

int hex_digit(char value)
{
  return value <= '9' ? value - '0' : value - 'a' + 10;
}

int main()
{
  try {
    int count;
    std::cin >> count;
    int statefulOutput = 9;
    for (int i = 0; i < count; ++i) {
      std::string encoded, text;
      int initial;
      std::cin >> encoded >> initial;
      if (encoded != "-") {
        for (std::size_t j = 0; j < encoded.size(); j += 2) {
          text += static_cast<char>(16 * hex_digit(encoded[j]) + hex_digit(encoded[j + 1]));
        }
      }
      const auto saved = text;
      for (int start : std::array<int, 3>{initial, std::numeric_limits<int>::min(),
                                         std::numeric_limits<int>::max()}) {
        int output = start;
        bool accepted = aim::b1::parse_i32(text, output);
        CHECK(text == saved);
        std::cout << accepted << ' ' << output << ' ';
      }
      bool accepted = aim::b1::parse_i32(text, statefulOutput);
      CHECK(text == saved);
      std::cout << accepted << ' ' << statefulOutput << '\n';
    }
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
'''


def reference(text):
    if GRAMMAR.fullmatch(text) is None:
        return None
    value = int(text)
    return value if MIN_VALUE <= value <= MAX_VALUE else None


def padded(value, rng):
    if value < 0:
        sign = b'-'
    elif value == 0:
        sign = rng.choice([b'', b'+', b'-'])
    else:
        sign = rng.choice([b'', b'+'])
    digits = str(abs(value)).encode('ascii')
    zeros = rng.randrange(1001 - len(sign) - len(digits))
    return sign + b'0' * zeros + digits


def make_cases():
    rng = random.Random(SEED)
    edges = [MIN_VALUE - 2, MIN_VALUE - 1, MIN_VALUE, MIN_VALUE + 1,
             -1, 0, 1, MAX_VALUE - 1, MAX_VALUE, MAX_VALUE + 1, MAX_VALUE + 2]
    invalid_parts = [b' ', b'\t', b'\n', b'\r', b'\0', b'\x80', b'\xff',
                     b'.', b'x', b'++', b'--']
    syntax_edges = [b'', b'+', b'-', b' 1', b'1 ', b'\t2', b'1\n',
                    b'\xef\xbc\x91', b'\xd9\xa1', b'1e3', b'0x10',
                    b'++1', b'--1', b'+-1', b'12\0']
    cases = []
    for index in range(RANDOM_CASES):
        mode = index % len(MODES)
        if mode == 0:
            text = padded(rng.randint(MIN_VALUE, MAX_VALUE), rng)
        elif mode == 1:
            text = padded(rng.choice(edges), rng)
        elif mode == 2:
            value = rng.choice([MIN_VALUE, MAX_VALUE, -1, 0, 1,
                                rng.randint(MIN_VALUE, MAX_VALUE)])
            text = padded(value, rng)
        elif mode == 3:
            value = rng.randint(2 ** 31 + 1, 10 ** 40) * rng.choice([-1, 1])
            text = padded(value, rng)
        elif mode == 4:
            base = padded(rng.randint(MIN_VALUE, MAX_VALUE), rng)[:998]
            position = rng.randrange(len(base) + 1)
            text = base[:position] + \
                rng.choice(invalid_parts) + base[position:]
        elif mode == 5:
            text = bytes(rng.randrange(256)
                         for _ in range(rng.randrange(1001)))
        elif mode == 6:
            text = rng.choice(syntax_edges)
        else:
            sign = rng.choice([b'', b'+', b'-', b'++'])
            digits = bytes(rng.choice(b'0123456789')
                           for _ in range(rng.randrange(1001 - len(sign))))
            text = sign + digits
        if index % 101 == 0 and len(text) < 1000:
            zeros = b'0' * (1000 - len(text))
            if GRAMMAR.fullmatch(text) and text[:1] in (b'+', b'-'):
                text = text[:1] + zeros + text[1:]
            elif text:
                text = zeros + text
            else:
                text = b'0' * 999 + b'x'
        initial = rng.choice([0, 9, MIN_VALUE, MAX_VALUE,
                              rng.randint(MIN_VALUE, MAX_VALUE)])
        cases.append((text, initial))
    return cases


def main():
    cases = make_cases()
    expected = []
    payload = [str(len(cases))]
    stateful_output = 9
    accepted = syntax_invalid = out_of_range = 0
    for text, initial in cases:
        parsed = reference(text)
        success = parsed is not None
        if success:
            accepted += 1
        elif GRAMMAR.fullmatch(text) is None:
            syntax_invalid += 1
        else:
            out_of_range += 1
        wanted = []
        for start in (initial, MIN_VALUE, MAX_VALUE):
            wanted.extend([int(success), parsed if success else start])
        if success:
            stateful_output = parsed
        wanted.extend([int(success), stateful_output])
        expected.append(wanted)
        payload.append(f'{text.hex() or "-"} {initial}')

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='b1-validation-') as directory:
        harness = Path(directory) / 'b1_driver.cpp'
        binary = Path(directory) / 'b1_driver.exe'
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
            raise AssertionError(f'Case {index}: input={cases[index]!r}, '
                                 f'expected={wanted!r}, actual={line!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    max_length = sum(len(text) == 1000 for text, _ in cases)
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_cases': len(cases),
        'cpp_calls': 4 * len(cases),
        'stateful_calls': len(cases),
        'accepted_cases': accepted,
        'syntax_invalid_cases': syntax_invalid,
        'out_of_range_cases': out_of_range,
        'failure_output_checks': 4 * (syntax_invalid + out_of_range),
        'input_unchanged_checks': 4 * len(cases),
        'max_length_cases': max_length,
        'modes': {mode: RANDOM_CASES // len(MODES) for mode in MODES},
        'reference': 'ASCII byte regex, Python int, explicit signed 32-bit bounds',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/b1-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'B1 validation passed: {len(cases)} random cases, '
          f'{4 * len(cases)} calls, {len(cases)} stateful calls '
          f'({max_length} maximum-length cases, seed {SEED})')


if __name__ == '__main__':
    main()
