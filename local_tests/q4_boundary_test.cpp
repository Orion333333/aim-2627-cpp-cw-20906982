// Check the maximum line count and long numeric fields from the contract.
#define main q4_public_main
#include "../src/main/A1_q4.cpp"
#undef main

void check_batch(const std::vector<std::string>& lines, long long expectedValue,
                 int expectedAccepted, int expectedRejected)
{
  CHECK(lines.size() == 10000);
  CommandResult result = execute(lines);
  CHECK(result.value == expectedValue);
  CHECK(result.accepted == expectedAccepted);
  CHECK(result.rejected == expectedRejected);
  CHECK(result.accepted + result.rejected == 10000);
}

int main()
{
  try {
    std::vector<std::string> lines(10000, "ADD 1");
    check_batch(lines, 10000, 10000, 0);

    lines.assign(10000, "");
    check_batch(lines, 0, 0, 10000);

    lines.clear();
    for (int i = 0; i < 2500; ++i) {
      lines.insert(lines.end(), {"SET 1000000", "ADD 1", "RESET", "ADD -1000000"});
    }
    check_batch(lines, -1000000, 7500, 2500);

    lines.clear();
    for (int i = 0; i < 2500; ++i) {
      lines.insert(lines.end(), {"SET -1000000", "ADD -1", "RESET", "ADD 1000000"});
    }
    check_batch(lines, 1000000, 7500, 2500);

    lines.assign(10000, "RESET x");
    lines[0] = "SET 5";
    check_batch(lines, 5, 1, 9999);

    lines.assign(10000, "RESET");
    check_batch(lines, 0, 10000, 0);

    lines.assign(10000, "ADD 1");
    lines[0] = "SET " + std::string(10000, '9');
    check_batch(lines, 9999, 9999, 1);

    lines.assign(10000, "ADD 0");
    lines[0] = "SET +" + std::string(10000, '0') + "1";
    lines[1] = "ADD 1.0";
    lines[2] = "RESET x";
    check_batch(lines, 1, 9998, 2);

    std::cout << "Q4 boundary tests passed (8 batches, 10000 lines each, "
                 "10000-digit numeric fields)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
