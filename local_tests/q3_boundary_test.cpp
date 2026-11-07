// Exercise the published input limits using mathematically known results.
#define main q3_public_main
#include "../src/main/A1_q3.cpp"
#undef main

void check_indices(const std::vector<int>& result, int first, int count)
{
  CHECK(result.size() == static_cast<std::size_t>(count));
  for (int i = 0; i < count; ++i) {
    CHECK(result[i] == first + i);
  }
}

int main()
{
  try {
    int count = 200000;
    int half = count / 2;
    long long total = 1LL * count * 1000000000;
    std::vector<int> positive(count, 1000000000);
    std::vector<int> negative(count, -1000000000);

    CHECK(alarms(positive, count, total).empty());
    check_indices(alarms(positive, count, total - 1), count - 1, 1);
    CHECK(alarms(negative, count, -total).empty());
    check_indices(alarms(negative, count, -total - 1), count - 1, 1);

    check_indices(alarms(positive, 1, 0), 0, count);
    check_indices(alarms(positive, half, total / 2 - 1), half - 1,
                  count - half + 1);

    std::vector<int> alternating(count);
    for (int i = 0; i < count; ++i) {
      alternating[i] = (i % 2 == 0) ? 1000000000 : -1000000000;
    }
    CHECK(alarms(alternating, half, 0).empty());
    check_indices(alarms(alternating, half, -1), half - 1,
                  count - half + 1);

    std::cout << "Q3 boundary tests passed (8 cases, n=200000, "
                 "max output=200000)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
