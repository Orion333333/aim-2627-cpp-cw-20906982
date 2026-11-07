// Check the published dimensions using maps with known complete results.
#define main q5_public_main
#include "../src/main/A1_q5.cpp"
#undef main

void check_uniform(const std::vector<std::vector<int>>& result, int expected)
{
  CHECK(result.size() == 300);
  for (const std::vector<int>& row : result) {
    CHECK(row.size() == 300);
    for (int value : row) {
      CHECK(value == expected);
    }
  }
}

int main()
{
  try {
    std::vector<std::string> grid(300, std::string(300, '.'));
    check_uniform(risk(grid), 0);

    grid.assign(300, std::string(300, '#'));
    check_uniform(risk(grid), -1);

    for (int row = 0; row < 300; ++row) {
      for (int column = 0; column < 300; ++column) {
        grid[row][column] = ((row + column) % 2 == 0) ? '#' : '.';
      }
    }
    std::vector<std::vector<int>> result = risk(grid);
    CHECK(result.size() == 300);
    for (int row = 0; row < 300; ++row) {
      CHECK(result[row].size() == 300);
      for (int column = 0; column < 300; ++column) {
        int expected = -1;
        if ((row + column) % 2 != 0) {
          expected = 4 - (row == 0) - (row == 299) -
                     (column == 0) - (column == 299);
        }
        CHECK(result[row][column] == expected);
      }
    }

    std::string longRow(300, '.');
    longRow[149] = '#';
    std::vector<std::vector<int>> rowExpected(1, std::vector<int>(300, 0));
    rowExpected[0][148] = 1;
    rowExpected[0][149] = -1;
    rowExpected[0][150] = 1;
    CHECK(risk({longRow}) == rowExpected);

    std::vector<std::string> longColumn(300, ".");
    longColumn[149] = "#";
    std::vector<std::vector<int>> columnExpected(300, std::vector<int>(1, 0));
    columnExpected[148][0] = 1;
    columnExpected[149][0] = -1;
    columnExpected[150][0] = 1;
    CHECK(risk(longColumn) == columnExpected);

    grid.assign(300, std::string(300, '.'));
    grid[299][299] = 'x';
    EXPECT_INVALID(risk(grid));

    grid.assign(300, std::string(300, '.'));
    grid[299].pop_back();
    EXPECT_INVALID(risk(grid));

    EXPECT_INVALID(risk(std::vector<std::string>(300, "")));

    std::cout << "Q5 boundary tests passed (8 cases, max 300x300, "
                 "90000 cells)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
