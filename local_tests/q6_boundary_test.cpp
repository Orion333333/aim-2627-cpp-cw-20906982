// Check maximum-size inputs with independently known winners.
#define main q6_public_main
#include "../src/main/A1_q6.cpp"
#undef main

void check_case(const char* name, const std::vector<Target>& targets, int range, int expected)
{
  const std::vector<Target> saved = targets;
  int actual = select_target(targets, range);
  if (actual != expected) {
    throw std::runtime_error(std::string(name) + ": expected " +
                             std::to_string(expected) + ", got " + std::to_string(actual));
  }
  CHECK(targets.size() == saved.size());
  for (std::size_t i = 0; i < targets.size(); ++i) {
    CHECK(targets[i].id == saved[i].id && targets[i].x == saved[i].x &&
          targets[i].y == saved[i].y && targets[i].hp == saved[i].hp &&
          targets[i].visible == saved[i].visible);
  }
}

int main()
{
  try {
    const int COUNT = 100000;
    std::vector<Target> targets(COUNT);
    for (int i = 0; i < COUNT; ++i) {
      targets[i] = {i, 0, 0, 100, false};
    }
    check_case("all invisible", targets, 1000000, -1);

    for (Target& target : targets) {
      target.visible = true;
      target.hp = (target.id % 2 == 0) ? 0 : -100;
    }
    check_case("all depleted", targets, 1000000, -1);

    for (Target& target : targets) {
      target.hp = 1;
      target.x = 1000000;
      target.y = -1000000;
    }
    check_case("all outside wide circle", targets, 1000000, -1);

    for (Target& target : targets) {
      target.hp = 100;
      target.x = 0;
      target.y = 0;
    }
    targets.back() = {COUNT - 1, -600000, 800000, 1, true};
    check_case("lowest hp at last position", targets, 1000000, COUNT - 1);

    for (Target& target : targets) {
      target.hp = 1;
      target.x = -1000000;
      target.y = 0;
    }
    targets.back() = {COUNT - 1, 0, 0, 1, true};
    check_case("nearest at last position", targets, 1000000, COUNT - 1);

    for (int i = 0; i < COUNT; ++i) {
      targets[i] = {COUNT - 1 - i, 0, 0, 1, true};
    }
    check_case("descending tied ids", targets, 0, 0);

    std::reverse(targets.begin(), targets.end());
    check_case("ascending tied ids", targets, 0, 0);

    for (int i = 0; i < COUNT; ++i) {
      targets[i] = {i, 0, 0, 1, true};
      if (i % 3 == 0) {
        targets[i].visible = false;
      } else if (i % 3 == 1) {
        targets[i].hp = -100;
      } else {
        targets[i].x = 1000000;
        targets[i].y = 1000000;
      }
    }
    targets.back() = {COUNT - 1, -600000, -800000, 100, true};
    check_case("only eligible target at end", targets, 1000000, COUNT - 1);

    std::cout << "Q6 boundary tests passed (8 cases, n=100000 each)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
