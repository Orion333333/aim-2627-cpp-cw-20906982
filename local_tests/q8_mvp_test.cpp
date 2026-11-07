// Reuse the saved implementation and its fixed types.
#define main q8_public_main
#include "../src/main/A1_q8.cpp"
#undef main

int main()
{
  try {
    int checks = 0;
    auto expect = [&checks](const char* name, const std::vector<Telemetry>& frames,
                           Summary expected) {
      const std::vector<Telemetry> saved = frames;
      Summary actual = summarize(frames);
      if (actual.valid != expected.valid || actual.duplicate != expected.duplicate ||
          actual.invalid != expected.invalid || actual.total_hp != expected.total_hp ||
          actual.ids != expected.ids) {
        std::ostringstream message;
        message << name << ": got {" << actual.valid << ',' << actual.duplicate << ','
                << actual.invalid << ',' << actual.total_hp << ", ids:";
        for (int id : actual.ids) {
          message << ' ' << id;
        }
        message << '}';
        throw std::runtime_error(message.str());
      }
      CHECK(actual.valid + actual.duplicate + actual.invalid == static_cast<int>(frames.size()));
      CHECK(actual.valid == static_cast<int>(actual.ids.size()));
      CHECK(actual.valid >= 0 && actual.duplicate >= 0 && actual.invalid >= 0);
      CHECK(actual.total_hp >= 0 && actual.total_hp <= 100LL * actual.valid);
      CHECK(std::is_sorted(actual.ids.begin(), actual.ids.end()));
      CHECK(std::adjacent_find(actual.ids.begin(), actual.ids.end()) == actual.ids.end());
      CHECK(frames.size() == saved.size());
      for (std::size_t i = 0; i < frames.size(); ++i) {
        CHECK(frames[i].id == saved[i].id && frames[i].hp == saved[i].hp);
      }
      ++checks;
    };

    expect("public mixed records", {{2, 200}, {1, -5}, {2, 10}, {-1, 30}},
           {2, 1, 1, 100, {1, 2}});
    expect("public validation order", {{1, -1001}, {1, 30}, {1, 1001}},
           {1, 0, 2, 30, {1}});
    expect("empty", {}, {0, 0, 0, 0, {}});
    expect("minimum id", {{0, 0}}, {1, 0, 0, 0, {0}});
    expect("maximum id", {{9999, 100}}, {1, 0, 0, 100, {9999}});
    expect("negative id", {{-1, 30}}, {0, 0, 1, 0, {}});
    expect("id above range", {{10000, 30}}, {0, 0, 1, 0, {}});
    expect("minimum int id", {{std::numeric_limits<int>::min(), 30}}, {0, 0, 1, 0, {}});
    expect("maximum int id", {{std::numeric_limits<int>::max(), 30}}, {0, 0, 1, 0, {}});
    expect("minimum accepted hp", {{1, -1000}}, {1, 0, 0, 0, {1}});
    expect("maximum accepted hp", {{1, 1000}}, {1, 0, 0, 100, {1}});
    expect("hp below range", {{1, -1001}}, {0, 0, 1, 0, {}});
    expect("hp above range", {{1, 1001}}, {0, 0, 1, 0, {}});
    expect("minimum int hp", {{1, std::numeric_limits<int>::min()}}, {0, 0, 1, 0, {}});
    expect("maximum int hp", {{1, std::numeric_limits<int>::max()}}, {0, 0, 1, 0, {}});
    expect("negative hp is valid", {{1, -1}}, {1, 0, 0, 0, {1}});
    expect("hp below clamp limit", {{1, 99}}, {1, 0, 0, 99, {1}});
    expect("hp above clamp limit", {{1, 101}}, {1, 0, 0, 100, {1}});
    expect("first valid hp wins", {{1, 20}, {1, 99}}, {1, 1, 0, 20, {1}});
    expect("zero contribution still reserves id", {{1, -5}, {1, 100}}, {1, 1, 0, 0, {1}});
    expect("duplicate cannot lower total", {{1, 1000}, {1, 0}}, {1, 1, 0, 100, {1}});
    expect("invalid hp does not reserve id", {{1, -1001}, {1, 30}}, {1, 0, 1, 30, {1}});
    expect("seen id with low invalid hp", {{1, 20}, {1, -1001}}, {1, 0, 1, 20, {1}});
    expect("seen id with high invalid hp", {{1, 20}, {1, 1001}}, {1, 0, 1, 20, {1}});
    expect("ids sorted independently of arrival", {{9999, 50}, {2, 100}, {0, -1000}, {1, 10}},
           {4, 0, 0, 160, {0, 1, 2, 9999}});
    expect("both fields invalid counted once", {{-1, -1001}, {10000, 1001}}, {0, 0, 2, 0, {}});
    expect("mixed reuse and invalid hp", {{3, -1001}, {3, 200}, {3, 80}, {3, 1001},
                                         {4, -5}, {4, 4}},
           {2, 2, 2, 100, {3, 4}});
    expect("repeated invalid ids", {{-1, 10}, {-1, 20}, {10000, 10}}, {0, 0, 3, 0, {}});
    expect("input fields and order", {{8, 90}, {3, 20}, {8, 0}, {2, 1001}},
           {2, 1, 1, 110, {3, 8}});
    expect("independent reused id", {{8, 7}}, {1, 0, 0, 7, {8}});
    expect("independent empty call", {}, {0, 0, 0, 0, {}});
    expect("independent repeated call", {{2, 200}, {1, -5}, {2, 10}, {-1, 30}},
           {2, 1, 1, 100, {1, 2}});

    std::cout << "Q8 MVP tests passed (" << checks << " checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
