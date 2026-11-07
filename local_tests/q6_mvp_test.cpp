// Reuse the saved implementation and its fixed types.
#define main q6_public_main
#include "../src/main/A1_q6.cpp"
#undef main

int main()
{
  try {
    int checks = 0;
    auto expect = [&checks](const char* name, const std::vector<Target>& targets,
                            int range, int expected) {
      int actual = select_target(targets, range);
      if (actual != expected) {
        throw std::runtime_error(std::string(name) + ": expected " +
                                 std::to_string(expected) + ", got " + std::to_string(actual));
      }
      ++checks;
    };

    expect("public tie", {{7, 3, 4, 20, true}, {2, 0, 5, 20, true}}, 5, 2);
    expect("empty", {}, 5, -1);
    expect("negative range", {{7, 0, 0, 1, true}}, -1, -1);
    expect("minimum range", {{7, 0, 0, 1, true}}, std::numeric_limits<int>::min(), -1);
    expect("invisible", {{7, 0, 0, 1, false}}, 5, -1);
    expect("zero hp", {{7, 0, 0, 0, true}}, 5, -1);
    expect("negative hp", {{7, 0, 0, -100, true}}, 5, -1);
    expect("out of range", {{7, 3, 4, 1, true}}, 4, -1);
    expect("mixed filters", {{1, 0, 0, 1, false}, {2, 0, 0, 0, true},
                             {3, 6, 0, 1, true}, {42, 3, 4, 100, true}},
           5, 42);
    expect("hp before distance", {{7, 3, 4, 1, true}, {2, 0, 0, 2, true}}, 5, 7);
    expect("hp before id", {{1, 0, 0, 100, true}, {99, 3, 4, 1, true}}, 5, 99);
    expect("distance before id", {{1, 3, 4, 20, true}, {99, 1, 0, 20, true}}, 5, 99);
    expect("id breaks tie", {{9, 0, 0, 3, true}, {1, 0, 0, 3, true}}, 0, 1);
    expect("reversed tie", {{1, 0, 0, 3, true}, {9, 0, 0, 3, true}}, 0, 1);
    expect("zero id", {{0, 0, 0, 1, true}, {8, 0, 0, 2, true}}, 0, 0);
    expect("maximum id", {{std::numeric_limits<int>::max(), 0, 0, 1, true}},
           0, std::numeric_limits<int>::max());
    expect("zero range origin", {{31, 0, 0, 1, true}}, 0, 31);
    expect("zero range other point", {{31, 0, 1, 1, true}}, 0, -1);
    expect("negative coordinates", {{69, -3, -4, 1, true}}, 5, 69);
    expect("outside circle", {{69, 3, 5, 1, true}}, 5, -1);
    expect("million x", {{81, 1000000, 0, 1, true}}, 1000000, 81);
    expect("million negative y", {{82, 0, -1000000, 1, true}}, 1000000, 82);
    expect("wide sum", {{83, 1000000, 1000000, 1, true}}, 1000000, -1);
    expect("wide multiplication", {{84, 30000, 40000, 2, true}, {1, 50000, 1, 1, true}},
           50000, 84);
    expect("all filtered", {{1, 0, 0, -1, true}, {2, 0, 0, 2, false},
                            {3, 2, 2, 1, true}},
           1, -1);

    std::vector<Target> targets = {{90, 3, 4, 10, true}, {70, -3, -4, 10, true},
                                   {10, 1, 0, 20, true}};
    const std::vector<Target> saved = targets;
    expect("input order", targets, 5, 70);
    bool unchanged = targets.size() == saved.size();
    for (std::size_t i = 0; i < targets.size(); ++i) {
      unchanged = unchanged && targets[i].id == saved[i].id && targets[i].x == saved[i].x &&
                  targets[i].y == saved[i].y && targets[i].hp == saved[i].hp &&
                  targets[i].visible == saved[i].visible;
    }
    CHECK(unchanged);
    ++checks;
    std::reverse(targets.begin(), targets.end());
    expect("reversed input", targets, 5, 70);
    expect("independent no candidate", {}, 5, -1);
    expect("independent new candidate", {{123, 0, 0, 100, true}}, 0, 123);

    std::cout << "Q6 MVP tests passed (" << checks << " checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
