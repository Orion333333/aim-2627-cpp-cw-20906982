// Reuse the saved implementation without changing the public test entry point.
#define main q4_public_main
#include "../src/main/A1_q4.cpp"
#undef main

void check_result(const std::vector<std::string>& lines, long long expectedValue,
                  int expectedAccepted, int expectedRejected)
{
  CommandResult result = execute(lines);
  CHECK(result.value == expectedValue);
  CHECK(result.accepted == expectedAccepted);
  CHECK(result.rejected == expectedRejected);
  CHECK(result.accepted + result.rejected == static_cast<int>(lines.size()));
}

int main()
{
  try {
    check_result({}, 0, 0, 0);
    check_result({"ADD 5", "SET 8 x", "RESET", "ADD -2"}, -2, 3, 1);
    check_result({"SET 1000000", "ADD 1"}, 1000000, 1, 1);
    check_result({"SET -1000000", "ADD -1"}, -1000000, 1, 1);
    check_result({"SET 5", "RESET x"}, 5, 1, 1);
    check_result({"add 5", "", " \t"}, 0, 0, 3);
    check_result({"ADD +2", "RESET"}, 0, 2, 0);
    check_result({" \tSET -7\r\n", " ADD +2 \t", "RESET \v\f"}, 0, 3, 0);
    check_result({"ADD", "SET"}, 0, 0, 2);
    check_result({"ADD 1 2", "SET 3 x"}, 0, 0, 2);
    check_result({"ADD 1.0", "SET 2.5"}, 0, 0, 2);
    check_result({"ADD 12x", "SET 0x10"}, 0, 0, 2);
    check_result({"MUL 2", "RESETx"}, 0, 0, 2);
    check_result({"SET 1000001", "ADD -1000001"}, 0, 0, 2);
    check_result({"SET 9223372036854775808", "ADD -9223372036854775809"},
                 0, 0, 2);
    check_result({"ADD +0", "SET -0", "RESET"}, 0, 3, 0);
    check_result({"SET 00012", "ADD -0002"}, 10, 2, 0);
    check_result({"ADD +", "SET --1", "ADD +-1", "SET + 1"}, 0, 0, 4);
    check_result({"SET 1000000", "ADD 1", "RESET", "ADD 2"}, 2, 3, 1);
    check_result({"SET 10", "ADD 3 junk", "ADD -4"}, 6, 2, 1);
    check_result({"RESET", "RESET", "SET 0", "ADD 0"}, 0, 4, 0);
    check_result({"SET -1000000", "ADD 1000000", "SET 1000000",
                  "ADD -1000000"}, 0, 4, 0);
    check_result({"ADD+2", "SET-1"}, 0, 0, 2);
    check_result({"SET 1000000", "ADD -1000001"}, 1000000, 1, 1);

    std::vector<std::string> lines = {"SET 5", "RESET x", "ADD -2"};
    std::vector<std::string> original = lines;
    check_result(lines, 3, 2, 1);
    CHECK(lines == original);

    std::cout << "Q4 MVP tests passed (25 command sequences, input unchanged)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
