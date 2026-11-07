// Reuse the saved implementation and its fixed types.
#define main q7_public_main
#include "../src/main/A1_q7.cpp"
#undef main

int main()
{
  try {
    int checks = 0;
    auto expect = [&checks](const char* name, int ammo, int heat, int cool, int shotHeat,
                           const std::vector<int>& requests, FireResult expected) {
      const std::vector<int> saved = requests;
      FireResult actual = simulate(ammo, heat, cool, shotHeat, requests);
      if (actual.shots != expected.shots || actual.rejected != expected.rejected ||
          actual.ammo != expected.ammo || actual.heat != expected.heat) {
        std::ostringstream message;
        message << name << ": expected {" << expected.shots << ',' << expected.rejected << ','
                << expected.ammo << ',' << expected.heat << "}, got {" << actual.shots << ','
                << actual.rejected << ',' << actual.ammo << ',' << actual.heat << '}';
        throw std::runtime_error(message.str());
      }
      CHECK(requests == saved);
      CHECK(actual.shots + actual.rejected == std::count(requests.begin(), requests.end(), 1));
      CHECK(actual.ammo == ammo - actual.shots);
      CHECK(actual.heat >= 0 && actual.heat <= 100);
      CHECK(actual.shots >= 0 && actual.rejected >= 0 && actual.ammo >= 0);
      ++checks;
    };

    expect("public mixed requests", 2, 90, 10, 20, {1, 1, 1}, {2, 1, 0, 100});
    expect("public idle frame", 3, 100, 20, 10, {0}, {0, 0, 3, 80});
    expect("empty requests", 4, 80, 10, 30, {}, {0, 0, 4, 80});
    expect("empty with maximum cooling", 0, 100, 100, 100, {}, {0, 0, 0, 100});
    expect("cooling clamps to zero", 1, 5, 10, 20, {0}, {0, 0, 1, 0});
    expect("shot after cooling to zero", 1, 0, 10, 20, {1}, {1, 0, 0, 20});
    expect("cool before checking", 1, 100, 10, 10, {1}, {1, 0, 0, 100});
    expect("exact heat limit", 1, 90, 0, 10, {1}, {1, 0, 0, 100});
    expect("one over heat limit", 1, 91, 0, 10, {1}, {0, 1, 1, 91});
    expect("rejection retains cooling", 1, 100, 10, 11, {1}, {0, 1, 1, 90});
    expect("empty ammo still cools", 0, 50, 10, 20, {1}, {0, 1, 0, 40});
    expect("zero shot heat still needs ammo", 0, 100, 0, 0, {1}, {0, 1, 0, 100});
    expect("zero shot heat at limit", 1, 100, 0, 0, {1}, {1, 0, 0, 100});
    expect("no cooling", 3, 0, 0, 50, {1, 1, 1}, {2, 1, 1, 100});
    expect("zero shot heat consumes ammo", 2, 30, 10, 0, {1, 1, 1}, {2, 1, 0, 0});
    expect("all idle frames", 5, 25, 10, 100, {0, 0, 0, 0}, {0, 0, 5, 0});
    expect("idle at heat limit", 4, 100, 0, 100, {0, 0}, {0, 0, 4, 100});
    expect("recovery after rejection", 1, 100, 10, 20, {1, 1}, {1, 1, 0, 100});
    expect("repeated heat rejections", 3, 100, 0, 1, {1, 1, 1}, {0, 3, 3, 100});
    expect("idle and rejected empty ammo", 0, 50, 20, 100, {0, 1, 0, 1}, {0, 2, 0, 0});
    expect("maximum cooling and shot heat", 3, 100, 100, 100, {1, 1, 1}, {3, 0, 0, 100});
    expect("last frame cools after ammo runs out", 1, 0, 10, 100, {1, 0}, {1, 0, 0, 90});
    expect("idle between shots", 2, 95, 10, 20, {0, 1, 0, 1}, {2, 0, 0, 95});
    expect("ammo exhausted", 1, 0, 0, 10, {1, 1, 0, 1}, {1, 2, 0, 10});
    expect("maximum initial ammo", 100, 99, 1, 2, {1, 1, 1}, {2, 1, 98, 100});
    expect("zero cooling and shot heat", 3, 0, 0, 0, {0, 1, 0}, {1, 0, 2, 0});

    int ammo = 3;
    int heat = 99;
    int cool = 1;
    int shotHeat = 2;
    std::vector<int> requests = {1, 0, 1};
    expect("input state", ammo, heat, cool, shotHeat, requests, {2, 0, 1, 100});
    CHECK(ammo == 3 && heat == 99 && cool == 1 && shotHeat == 2);
    CHECK((requests == std::vector<int>{1, 0, 1}));
    ++checks;
    expect("independent empty call", 7, 40, 5, 80, {}, {0, 0, 7, 40});
    expect("independent repeated call", 2, 90, 10, 20, {1, 1, 1}, {2, 1, 0, 100});

    std::cout << "Q7 MVP tests passed (" << checks << " checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
