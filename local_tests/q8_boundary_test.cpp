// Check maximum-size batches and the complete legal ID domain.
#define main q8_public_main
#include "../src/main/A1_q8.cpp"
#undef main

void check_case(const char* name, const std::vector<Telemetry>& frames, const Summary& expected)
{
  CHECK(frames.size() == 20000);
  const std::vector<Telemetry> saved = frames;
  Summary actual = summarize(frames);
  if (actual.valid != expected.valid || actual.duplicate != expected.duplicate ||
      actual.invalid != expected.invalid || actual.total_hp != expected.total_hp ||
      actual.ids != expected.ids) {
    throw std::runtime_error(std::string(name) + ": unexpected summary");
  }
  CHECK(actual.valid + actual.duplicate + actual.invalid == 20000);
  CHECK(actual.valid == static_cast<int>(actual.ids.size()));
  CHECK(actual.total_hp >= 0 && actual.total_hp <= 100LL * actual.valid);
  CHECK(std::is_sorted(actual.ids.begin(), actual.ids.end()));
  CHECK(std::adjacent_find(actual.ids.begin(), actual.ids.end()) == actual.ids.end());
  CHECK(frames.size() == saved.size());
  for (std::size_t i = 0; i < frames.size(); ++i) {
    CHECK(frames[i].id == saved[i].id && frames[i].hp == saved[i].hp);
  }
}

int main()
{
  try {
    std::vector<int> allIds(10000);
    std::iota(allIds.begin(), allIds.end(), 0);
    std::vector<Telemetry> frames;
    frames.reserve(20000);

    for (int i = 0; i < 20000; ++i) {
      if (i % 2 == 0) {
        frames.push_back({std::numeric_limits<int>::min(), std::numeric_limits<int>::max()});
      } else {
        frames.push_back({std::numeric_limits<int>::max(), std::numeric_limits<int>::min()});
      }
    }
    check_case("all invalid extreme fields", frames, {0, 0, 20000, 0, {}});

    frames.assign(20000, Telemetry{9999, 1000});
    check_case("one valid id repeated", frames, {1, 19999, 0, 100, {9999}});

    frames.clear();
    for (int id = 9999; id >= 0; --id) {
      frames.push_back({id, 1000});
    }
    for (int id = 9999; id >= 0; --id) {
      frames.push_back({id, -1000});
    }
    check_case("full domain and maximum total", frames, {10000, 10000, 0, 1000000LL, allIds});

    frames.clear();
    for (int id = 0; id < 10000; ++id) {
      frames.push_back({id, -1000});
    }
    for (int id = 0; id < 10000; ++id) {
      frames.push_back({id, 1000});
    }
    check_case("valid negative hp reserves every id", frames, {10000, 10000, 0, 0, allIds});

    frames.clear();
    for (int id = 9999; id >= 0; --id) {
      frames.push_back({id, 1001});
    }
    for (int id = 9999; id >= 0; --id) {
      frames.push_back({id, 50});
    }
    check_case("invalid records before full domain", frames, {10000, 0, 10000, 500000, allIds});

    frames.clear();
    for (int id = 0; id < 10000; ++id) {
      frames.push_back({id, 30});
    }
    for (int id = 0; id < 10000; ++id) {
      frames.push_back({id, std::numeric_limits<int>::min()});
    }
    check_case("seen ids with invalid hp", frames, {10000, 0, 10000, 300000, allIds});

    frames.clear();
    for (int id = 0; id < 5000; ++id) {
      frames.push_back({id, -1001});
      frames.push_back({id, 101});
      frames.push_back({id, -5});
      frames.push_back({id + 10000, 30});
    }
    std::vector<int> halfIds(allIds.begin(), allIds.begin() + 5000);
    check_case("mixed classifications", frames, {5000, 5000, 10000, 500000, halfIds});

    frames.assign(20000, Telemetry{10000, 100});
    frames.back() = {0, 100};
    check_case("only the last record is valid", frames, {1, 0, 19999, 100, {0}});

    std::cout << "Q8 boundary tests passed (8 cases, 20000 records each, 10000 legal IDs)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
