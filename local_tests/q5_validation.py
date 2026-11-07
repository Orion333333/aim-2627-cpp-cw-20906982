"""Compare Q5 with an independent obstacle-to-neighbor reference model."""

import hashlib
import json
import random
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src/main/A1_q5.cpp'
SEED = 2627
RANDOM_CASES = 1000


def reference(grid):
    if not grid:
        return []
    columns = len(grid[0])
    if not columns or any(len(row) != columns for row in grid):
        return None
    if any(cell not in '.#' for row in grid for cell in row):
        return None
    result = [[-1 if cell == '#' else 0 for cell in row] for row in grid]
    for row, line in enumerate(grid):
        for column, cell in enumerate(line):
            if cell != '#':
                continue
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                target_row, target_column = row + dy, column + dx
                if (0 <= target_row < len(grid)
                        and 0 <= target_column < columns
                        and grid[target_row][target_column] == '.'):
                    result[target_row][target_column] += 1
    return result


def make_cases():
    rng = random.Random(SEED)
    cases = []
    for index in range(RANDOM_CASES):
        invalid = index % 4 == 0
        rows = rng.randint(1, 20) if invalid else rng.randrange(21)
        columns = rng.randint(1, 20)
        grid = [''.join(rng.choices('.#', k=columns)) for _ in range(rows)]
        if invalid:
            mode = rng.randrange(3)
            if mode == 0:
                grid = [''] * rows
            elif mode == 1:
                if len(grid) == 1:
                    grid.append('.' * columns)
                row = rng.randrange(1, len(grid))
                grid[row] = grid[row][:-1]
            else:
                row, column = rng.randrange(rows), rng.randrange(columns)
                line = list(grid[row])
                line[column] = rng.choice(['x', ' ', '0', '\0', '\n'])
                grid[row] = ''.join(line)
        cases.append(grid)
    return cases


def main():
    cases = make_cases()
    expected = [reference(grid) for grid in cases]
    valid_maps = sum(result is not None for result in expected)
    invalid_maps = len(cases) - valid_maps
    assert valid_maps == 750 and invalid_maps == 250
    payload = [str(len(cases))]
    for grid in cases:
        payload.append(str(len(grid)))
        payload.extend(row.encode('utf-8').hex() or '-' for row in grid)

    compiler = shutil.which('g++')
    if not compiler:
        raise RuntimeError('g++ was not found on PATH')
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory(prefix='q5-validation-') as directory:
        harness = Path(directory) / 'q5_driver.cpp'
        binary = Path(directory) / 'q5_driver.exe'
        harness.write_text(
            '#define main q5_public_main\n'
            f'#include "{SOURCE.as_posix()}"\n'
            '#undef main\n'
            'int main()\n'
            '{\n'
            '  int count;\n'
            '  std::cin >> count;\n'
            '  for (int i = 0; i < count; ++i) {\n'
            '    int rows;\n'
            '    std::cin >> rows;\n'
            '    std::vector<std::string> grid;\n'
            '    for (int j = 0; j < rows; ++j) {\n'
            '      std::string encoded, line;\n'
            '      std::cin >> encoded;\n'
            '      if (encoded != "-") {\n'
            '        for (std::size_t k = 0; k < encoded.size(); k += 2) {\n'
            '          int value = std::stoi(encoded.substr(k, 2),\n'
            '                                nullptr, 16);\n'
            '          line += static_cast<char>(value);\n'
            '        }\n'
            '      }\n'
            '      grid.push_back(line);\n'
            '    }\n'
            '    try {\n'
            '      auto result = aim::q5::risk(grid);\n'
            '      std::size_t columns = result.empty() ? 0 :\n'
            '                            result.front().size();\n'
            '      std::cout << "OK " << result.size() << \' \' << columns;\n'
            '      for (const auto& row : result) {\n'
            '        for (int value : row) {\n'
            "          std::cout << ' ' << value;\n"
            '        }\n'
            '      }\n'
            "      std::cout << '\\n';\n"
            '    } catch (const std::invalid_argument&) {\n'
            '      std::cout << "INVALID\\n";\n'
            '    }\n'
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
        if wanted is None:
            if line != 'INVALID':
                raise AssertionError(
                    f'Case {index}: expected invalid_argument')
            continue
        fields = line.split()
        dimensions = [len(wanted), len(wanted[0]) if wanted else 0]
        values = [value for row in wanted for value in row]
        if (not fields or fields[0] != 'OK'
                or list(map(int, fields[1:])) != dimensions + values):
            raise AssertionError(f'Case {index}: grid={cases[index]!r}, '
                                 f'expected={wanted!r}, actual={line!r}')
    assert source_hash == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    report = {
        'status': 'PASS',
        'source_sha256': source_hash,
        'seed': SEED,
        'random_maps': RANDOM_CASES,
        'valid_maps': valid_maps,
        'invalid_maps': invalid_maps,
        'reference': 'scatter each obstacle to neighboring open cells',
        'compiler': compiler,
        'compile_stderr': compiled.stderr,
    }
    output = ROOT / 'scores/q5-final/validation.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8')
    print(f'Q5 validation passed: {RANDOM_CASES} random maps '
          f'({valid_maps} valid, {invalid_maps} invalid, seed {SEED})')


if __name__ == '__main__':
    main()
