// Reuse the saved implementation without changing the public test entry point.
#define main q5_public_main
#include "../src/main/A1_q5.cpp"
#undef main

int main()
{
  try {
    CHECK((risk({".#", ".."}) == std::vector<std::vector<int>>{{1, -1}, {0, 1}}));
    CHECK(risk({}).empty());
    CHECK((risk({"."}) == std::vector<std::vector<int>>{{0}}));
    CHECK((risk({"#"}) == std::vector<std::vector<int>>{{-1}}));
    CHECK((risk({".#."}) == std::vector<std::vector<int>>{{1, -1, 1}}));
    CHECK((risk({".", "#", "."}) == std::vector<std::vector<int>>{{1}, {-1}, {1}}));
    CHECK((risk({"##", "##"}) ==
           std::vector<std::vector<int>>{{-1, -1}, {-1, -1}}));
    CHECK((risk({"..", ".."}) == std::vector<std::vector<int>>{{0, 0}, {0, 0}}));
    CHECK((risk({"#.", ".."}) == std::vector<std::vector<int>>{{-1, 1}, {1, 0}}));
    CHECK((risk({".#.", "#.#", ".#."}) ==
           std::vector<std::vector<int>>{{2, -1, 2}, {-1, 4, -1}, {2, -1, 2}}));
    CHECK((risk({"#..", ".#."}) ==
           std::vector<std::vector<int>>{{-1, 2, 0}, {2, -1, 1}}));

    EXPECT_INVALID(risk({""}));
    EXPECT_INVALID(risk({"", ""}));
    EXPECT_INVALID(risk({"..", "."}));
    EXPECT_INVALID(risk({".", ".."}));
    EXPECT_INVALID(risk({"x."}));
    EXPECT_INVALID(risk({"..", ".x"}));
    EXPECT_INVALID(risk({" ."}));

    std::vector<std::string> grid = {".#", ".."};
    CHECK((risk(grid) == std::vector<std::vector<int>>{{1, -1}, {0, 1}}));
    CHECK((grid == std::vector<std::string>{".#", ".."}));

    std::cout << "Q5 MVP tests passed (20 checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
