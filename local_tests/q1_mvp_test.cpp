// Reuse the saved implementation without changing the template's public main.
#define main q1_public_main
#include "../src/main/A1_q1.cpp"
#undef main

int main()
{
  try {
    CHECK(ratio(2, 3) == 66);
    CHECK(ratio(-5, 100) == 0);
    CHECK(ratio(200, 100) == 100);
    CHECK(ratio(10, 0) == -1);
    CHECK(ratio(10, -100) == -1);
    CHECK(ratio(0, 100) == 0);
    CHECK(ratio(100, 100) == 100);
    CHECK(ratio(999999999999LL, 1000000000000LL) == 99);
    CHECK(ratio(1000000000000LL, 1000000000000LL) == 100);

    CHECK(report(7, 2, 3, 19) == "ID=7;HP=66;BAT=19;STATE=LOW");
    CHECK(report(7, 2, 3, 20) == "ID=7;HP=66;BAT=20;STATE=WARNING");
    CHECK(report(7, 2, 3, 59) == "ID=7;HP=66;BAT=59;STATE=WARNING");
    CHECK(report(7, 2, 3, 60) == "ID=7;HP=66;BAT=60;STATE=OK");
    CHECK(report(0, 4, 0, -7) == "ID=0;HP=INVALID;BAT=0;STATE=LOW");
    CHECK(report(9999, 4, -1, std::numeric_limits<int>::max()) ==
          "ID=9999;HP=INVALID;BAT=100;STATE=OK");
    CHECK(report(0, -5, 100, std::numeric_limits<int>::min()) ==
          "ID=0;HP=0;BAT=0;STATE=LOW");
    CHECK(report(7, 200, 100, 101) == "ID=7;HP=100;BAT=100;STATE=OK");

    CHECK(ratio(-1000000000000LL, 1) == 0);
    CHECK(ratio(1000000000000LL, 1) == 100);
    CHECK(ratio(1000000000000LL, -1000000000000LL) == -1);
    CHECK(report(0, 0, 1, 0) == "ID=0;HP=0;BAT=0;STATE=LOW");
    CHECK(report(9999, 1, 1, 100) == "ID=9999;HP=100;BAT=100;STATE=OK");

    // An earlier invalid call must not affect a later valid report.
    CHECK(report(7, 2, 3, 20) == "ID=7;HP=66;BAT=20;STATE=WARNING");

    int id = 7;
    long long hp = -5;
    long long maxHp = 100;
    int battery = -7;
    CHECK(report(id, hp, maxHp, battery) == "ID=7;HP=0;BAT=0;STATE=LOW");
    CHECK(id == 7 && hp == -5 && maxHp == 100 && battery == -7);

    // Check the mathematical floor bounds without reproducing the division.
    int exhaustiveCases = 0;
    for (long long maximum = 1; maximum <= 100; ++maximum) {
      for (long long health = -1; health <= maximum + 1; ++health) {
        long long normalized = std::max(0LL, std::min(health, maximum));
        long long percentage = ratio(health, maximum);
        CHECK(percentage >= 0 && percentage <= 100);
        CHECK(percentage * maximum <= normalized * 100 &&
              normalized * 100 < (percentage + 1) * maximum);
        ++exhaustiveCases;
      }
    }

    std::cout << "Q1 tests passed (25 directed checks, " << exhaustiveCases
              << " exhaustive cases)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
