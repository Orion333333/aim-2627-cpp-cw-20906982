// Reuse the saved implementation without changing the public test entry point.
#define main q3_public_main
#include "../src/main/A1_q3.cpp"
#undef main

int main()
{
  try {
    CHECK((alarms({1, 2, 3, 4}, 2, 4) == std::vector<int>{2, 3}));
    CHECK(alarms({}, 1, 0).empty());
    CHECK(alarms({1, 2}, 0, 0).empty());
    CHECK(alarms({1, 2}, -2, 0).empty());
    CHECK(alarms({1, 2}, 3, 0).empty());
    CHECK(alarms({1}, std::numeric_limits<int>::min(), 0).empty());
    CHECK(alarms({1}, std::numeric_limits<int>::max(), 0).empty());
    CHECK(alarms({2, 2}, 2, 4).empty());
    CHECK((alarms({-4, -3, -2}, 2, -6) == std::vector<int>{2}));
    CHECK((alarms({1, 2, 1}, 1, 1) == std::vector<int>{1}));
    CHECK((alarms({1, 2, 3}, 3, 5) == std::vector<int>{2}));
    CHECK(alarms({1, 2, 3}, 3, 6).empty());
    CHECK((alarms({0, 0, 0}, 2, -1) == std::vector<int>{1, 2}));
    CHECK((alarms({1000000000, 1000000000, 1000000000}, 3, 2500000000LL) ==
           std::vector<int>{2}));
    CHECK(alarms({-1000000000, -1000000000, -1000000000}, 3, -3000000000LL).empty());
    CHECK((alarms({1000000000, -1000000000, 1000000000, -1000000000}, 2, -1) ==
           std::vector<int>{1, 2, 3}));
    CHECK(alarms({1000000000, 1000000000}, 1, 1000000000000000LL).empty());
    CHECK((alarms({1, -1, 1}, 2, -1000000000000000LL) == std::vector<int>{1, 2}));

    std::vector<int> values = {1, 2, 3, 4};
    CHECK((alarms(values, 2, 4) == std::vector<int>{2, 3}));
    CHECK((values == std::vector<int>{1, 2, 3, 4}));

    std::cout << "Q3 MVP tests passed (20 checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
