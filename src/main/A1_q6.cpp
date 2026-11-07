#include <algorithm>
#include <array>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <limits>
#include <memory>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <type_traits>
#include <utility>
#include <vector>

// Assessment 01 Q6; see 题面.pdf.
namespace aim::q6 {
struct Target { int id; int x; int y; int hp; bool visible; };

// BEGIN IMPLEMENTATION
int select_target(const std::vector<Target>& targets, int max_range)
{
  if (max_range < 0) {
    return -1;
  }

  long long rangeSquared = 1LL * max_range * max_range;
  int bestId = -1;
  int bestHp = 0;
  long long bestDistance = 0;

  for (const Target& target : targets) {
    if (!target.visible || target.hp <= 0) {
      continue;
    }
    long long x = target.x;
    long long y = target.y;
    long long distanceSquared = x * x + y * y;
    if (distanceSquared > rangeSquared) {
      continue;
    }

    if (bestId == -1 || target.hp < bestHp ||
        (target.hp == bestHp &&
         (distanceSquared < bestDistance ||
          (distanceSquared == bestDistance && target.id < bestId)))) {
      bestId = target.id;
      bestHp = target.hp;
      bestDistance = distanceSquared;
    }
  }
  return bestId;
}
// END IMPLEMENTATION
}

#define CHECK(...) do { if (!(__VA_ARGS__)) throw std::runtime_error("check failed"); } while(false)
#define EXPECT_INVALID(...) do { bool caught=false; try { (void)(__VA_ARGS__); } catch(const std::invalid_argument&) { caught=true; } CHECK(caught); } while(false)
#define EXPECT_RANGE(...) do { bool caught=false; try { (void)(__VA_ARGS__); } catch(const std::out_of_range&) { caught=true; } CHECK(caught); } while(false)

using namespace aim::q6;
int main() {
    try {
        { CHECK(select_target({{7,3,4,20,true},{2,0,5,20,true}},5)==2); }
        { CHECK(select_target({},5)==-1); }
        std::cout << "PUBLIC 2/2\n";
    } catch(const std::exception& e) {
        std::cerr << e.what() << "\n";
        return 1;
    }
    return 0;
}
