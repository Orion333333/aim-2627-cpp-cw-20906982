#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <limits>
#include <memory>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <type_traits>
#include <utility>
#include <vector>

// Assessment 01 Q5; see 题面.pdf.
namespace aim::q5 {


// BEGIN IMPLEMENTATION
// aim-cpp-cw
std::vector<std::vector<int>> risk(const std::vector<std::string>& grid)
{
  if (grid.empty()) {
    return {};
  }

  std::size_t columns = grid.front().size();
  if (columns == 0) {
    throw std::invalid_argument("Grid rows must not be empty");
  }
  for (const std::string& line : grid) {
    if (line.size() != columns) {
      throw std::invalid_argument("Grid rows must have equal lengths");
    }
    for (char cell : line) {
      if (cell != '.' && cell != '#') {
        throw std::invalid_argument("Grid contains an invalid character");
      }
    }
  }

  int rowCount = static_cast<int>(grid.size());
  int columnCount = static_cast<int>(columns);
  std::vector<std::vector<int>> result(rowCount);
  for (int row = 0; row < rowCount; ++row) {
    result[row].resize(columnCount);
    for (int column = 0; column < columnCount; ++column) {
      if (grid[row][column] == '#') {
        result[row][column] = -1;
        continue;
      }
      if (row > 0 && grid[row - 1][column] == '#') {
        ++result[row][column];
      }
      if (row + 1 < rowCount && grid[row + 1][column] == '#') {
        ++result[row][column];
      }
      if (column > 0 && grid[row][column - 1] == '#') {
        ++result[row][column];
      }
      if (column + 1 < columnCount && grid[row][column + 1] == '#') {
        ++result[row][column];
      }
    }
  }

  return result;
}
// END IMPLEMENTATION
}

#define CHECK(...) do { if (!(__VA_ARGS__)) throw std::runtime_error("check failed"); } while(false)
#define EXPECT_INVALID(...) do { bool caught=false; try { (void)(__VA_ARGS__); } catch(const std::invalid_argument&) { caught=true; } CHECK(caught); } while(false)
#define EXPECT_RANGE(...) do { bool caught=false; try { (void)(__VA_ARGS__); } catch(const std::out_of_range&) { caught=true; } CHECK(caught); } while(false)

using namespace aim::q5;
int main() {
    try {
        { CHECK((risk({".#",".."})==std::vector<std::vector<int>>{{1,-1},{0,1}})); }
        { CHECK(risk({}).empty()); }
        std::cout << "PUBLIC 2/2\n";
    } catch(const std::exception& e) {
        std::cerr << e.what() << "\n";
        return 1;
    }
    return 0;
}
