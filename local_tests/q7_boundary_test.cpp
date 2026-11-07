// Check maximum-length request sequences with known final states.
#define main q7_public_main
#include "../src/main/A1_q7.cpp"
#undef main

void check_case(const char* name, int ammo, int heat, int cool, int shotHeat,
                const std::vector<int>& requests, FireResult expected)
{
  CHECK(requests.size() == 10000);
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
}

int main()
{
  try {
    std::vector<int> requests(10000, 0);
    check_case("all idle", 100, 100, 1, 100, requests, {0, 0, 100, 0});

    requests.assign(10000, 1);
    check_case("no ammo", 0, 100, 1, 100, requests, {0, 10000, 0, 0});
    check_case("overheated without cooling", 100, 100, 0, 1,
               requests, {0, 10000, 100, 100});
    check_case("zero shot heat", 100, 100, 0, 0, requests, {100, 9900, 0, 100});
    check_case("full cooling and shot heat", 100, 100, 100, 100,
               requests, {100, 9900, 0, 0});
    check_case("one shot every hundred frames", 100, 100, 1, 100,
               requests, {100, 9900, 0, 100});

    for (std::size_t i = 0; i < requests.size(); ++i) {
      requests[i] = (i % 2 == 0) ? 1 : 0;
    }
    check_case("alternating shots and idle frames", 100, 100, 50, 100,
               requests, {100, 4900, 0, 0});

    requests.assign(10000, 0);
    requests.back() = 1;
    check_case("only last frame requests a shot", 1, 100, 1, 100,
               requests, {1, 0, 0, 100});

    std::cout << "Q7 boundary tests passed (8 cases, 10000 frames each)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
