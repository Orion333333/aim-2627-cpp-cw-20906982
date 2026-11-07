// Check maximum-length arrays with analytically known stable prefixes.
#define main b2_public_main
#include "../src/main/A1_b2.cpp"
#undef main

void check_case(const char* name, const std::vector<int>& values, int low, int high,
                const std::vector<int>& expected)
{
  CHECK(values.size() == 200000);
  const int LEFT_GUARD = std::numeric_limits<int>::min();
  const int RIGHT_GUARD = std::numeric_limits<int>::max();
  std::vector<int> storage = {LEFT_GUARD};
  storage.insert(storage.end(), values.begin(), values.end());
  storage.push_back(RIGHT_GUARD);
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
  CHECK(storage.front() == LEFT_GUARD && storage.back() == RIGHT_GUARD);
  if (low > high) {
    CHECK(storage == saved);
  }
}

int main()
{
  try {
    const int COUNT = 200000;
    const int MIN_VALUE = std::numeric_limits<int>::min();
    const int MAX_VALUE = std::numeric_limits<int>::max();
    std::vector<int> values(COUNT);
    std::iota(values.begin(), values.end(), 0);
    std::reverse(values.begin(), values.end());
    check_case("all retained in descending order", values, MIN_VALUE, MAX_VALUE, values);

    values.assign(COUNT, 9);
    check_case("all removed", values, 0, 1, {});

    const std::array<int, 4> PATTERN = {3, 1, 3, 2};
    for (int i = 0; i < COUNT; ++i) {
      values[i] = PATTERN[i % 4];
    }
    std::vector<int> expected;
    for (int i = 0; i < COUNT / 4; ++i) {
      expected.insert(expected.end(), {3, 3, 2});
    }
    check_case("stable repeated pattern", values, 2, 3, expected);

    values.assign(COUNT, 7);
    check_case("equal bounds retain all duplicates", values, 7, 7, values);

    for (int i = 0; i < COUNT; ++i) {
      values[i] = (i % 2 == 0) ? MIN_VALUE : MAX_VALUE;
    }
    check_case("reversed extreme bounds", values, MAX_VALUE, MIN_VALUE, {});

    const std::array<int, 4> EXTREMES = {MAX_VALUE, MIN_VALUE, 0, MIN_VALUE};
    for (int i = 0; i < COUNT; ++i) {
      values[i] = EXTREMES[i % 4];
    }
    expected.assign(COUNT / 2, MIN_VALUE);
    check_case("minimum int endpoint", values, MIN_VALUE, MIN_VALUE, expected);

    values.assign(COUNT, MAX_VALUE);
    values.back() = MIN_VALUE;
    check_case("only the last value retained", values, MIN_VALUE, MIN_VALUE, {MIN_VALUE});

    values.assign(COUNT / 2, -1);
    expected.clear();
    for (int value = COUNT / 2; value > 0; --value) {
      values.push_back(value);
      expected.push_back(value);
    }
    check_case("large rejected prefix", values, 1, COUNT / 2, expected);

    std::cout << "B2 boundary tests passed (8 cases, 200000 elements each)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
