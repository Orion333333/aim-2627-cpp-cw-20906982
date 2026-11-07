// Check the kept prefix and guards without constraining the unspecified tail.
#define main b2_public_main
#include "../src/main/A1_b2.cpp"
#undef main

int main()
{
  try {
    const int MIN_VALUE = std::numeric_limits<int>::min();
    const int MAX_VALUE = std::numeric_limits<int>::max();
    int checks = 0;
    auto expect = [&](const char* name, const std::vector<int>& values, int low, int high,
                      const std::vector<int>& expected) {
      std::vector<int> storage = {MIN_VALUE};
      storage.insert(storage.end(), values.begin(), values.end());
      storage.push_back(MAX_VALUE);
      const auto saved = storage;
      int* data = storage.data() + 1;
      std::size_t kept = compact(data, values.size(), low, high);
      if (kept != expected.size()) {
        throw std::runtime_error(std::string(name) + ": unexpected kept count");
      }
      for (std::size_t i = 0; i < kept; ++i) {
        if (data[i] != expected[i]) {
          throw std::runtime_error(std::string(name) + ": unexpected prefix value");
        }
      }
      CHECK(storage.front() == MIN_VALUE && storage.back() == MAX_VALUE);
      if (low > high) {
        CHECK(storage == saved);
      }
      ++checks;
    };

    expect("public mixed values", {-1, 2, 0, 9}, 0, 2, {2, 0});
    expect("empty non-null range", {}, 0, 1, {});
    expect("all retained", {3, 1, 3, 2}, 1, 3, {3, 1, 3, 2});
    expect("all removed", {-3, -1, 9}, 0, 2, {});
    expect("duplicates remain stable", {3, 1, 3, 2, 3}, 2, 3, {3, 3, 2, 3});
    expect("equal bounds all retained", {1, 1, 1}, 1, 1, {1, 1, 1});
    expect("equal bounds mixed", {2, 1, 0, 1, 2}, 1, 1, {1, 1});
    expect("reversed bounds", {1, 2}, 5, 3, {});
    expect("reversed extreme bounds", {MAX_VALUE, MIN_VALUE, 0}, MAX_VALUE, MIN_VALUE, {});
    expect("one retained", {5}, 5, 5, {5});
    expect("one removed", {5}, 6, 7, {});
    expect("negative interval", {-3, -1, -2, 0}, -3, -1, {-3, -1, -2});
    expect("zero interval", {1, 0, -1, 0}, 0, 0, {0, 0});
    expect("both bounds included", {3, 0, 2, 1, -1}, 0, 2, {0, 2, 1});
    expect("only first retained", {1, 9, 8}, 1, 1, {1});
    expect("only last retained", {9, 8, 1}, 1, 1, {1});
    expect("alternating retained", {9, 2, 9, 1, 9, 2}, 1, 2, {2, 1, 2});
    expect("full int interval", {MIN_VALUE, MAX_VALUE, 0, -1, 1}, MIN_VALUE, MAX_VALUE,
           {MIN_VALUE, MAX_VALUE, 0, -1, 1});
    expect("minimum only", {MAX_VALUE, MIN_VALUE, 0, MIN_VALUE}, MIN_VALUE, MIN_VALUE,
           {MIN_VALUE, MIN_VALUE});
    expect("maximum only", {MIN_VALUE, MAX_VALUE, 0, MAX_VALUE}, MAX_VALUE, MAX_VALUE,
           {MAX_VALUE, MAX_VALUE});
    expect("extremes outside small interval", {MIN_VALUE, -1, 0, MAX_VALUE, 1}, -1, 1,
           {-1, 0, 1});
    expect("near minimum", {MIN_VALUE, MIN_VALUE + 1, MAX_VALUE}, MIN_VALUE, MIN_VALUE + 1,
           {MIN_VALUE, MIN_VALUE + 1});
    expect("near maximum", {MIN_VALUE, MAX_VALUE - 1, MAX_VALUE}, MAX_VALUE - 1, MAX_VALUE,
           {MAX_VALUE - 1, MAX_VALUE});
    expect("descending retained order", {5, 4, 3, 2, 1}, 2, 4, {4, 3, 2});
    expect("repeated retained pattern", {2, 1, 2, 1, 2, 1}, 1, 2, {2, 1, 2, 1, 2, 1});
    expect("removed ends", {10, 3, 1, 2, 20}, 1, 3, {3, 1, 2});
    expect("independent call", {9, 7, 9, 6}, 6, 7, {7, 6});

    CHECK(compact(nullptr, 0, 0, 1) == 0);
    ++checks;
    CHECK(compact(nullptr, 0, MIN_VALUE, MIN_VALUE) == 0);
    ++checks;
    CHECK(compact(nullptr, 0, MAX_VALUE, MIN_VALUE) == 0);
    ++checks;

    std::cout << "B2 MVP tests passed (" << checks << " checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
