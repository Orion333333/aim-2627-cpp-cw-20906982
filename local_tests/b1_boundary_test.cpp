// Check maximum-length inputs with several caller-owned output values.
#define main b1_public_main
#include "../src/main/A1_b1.cpp"
#undef main

int main()
{
  try {
    const int MIN_VALUE = std::numeric_limits<int>::min();
    const int MAX_VALUE = std::numeric_limits<int>::max();
    int cases = 0;
    int checks = 0;
    auto expect = [&](const char* name, const std::string& text, bool expectedSuccess,
                      int parsedValue = 0) {
      CHECK(text.size() == 1000);
      const std::string saved = text;
      for (int initial : std::array<int, 4>{0, 9, MIN_VALUE, MAX_VALUE}) {
        int output = initial;
        bool success = parse_i32(text, output);
        int wanted = expectedSuccess ? parsedValue : initial;
        if (success != expectedSuccess || output != wanted) {
          std::cerr << name << ": initial " << initial << ", expected " << expectedSuccess
                    << ',' << wanted << "; got " << success << ',' << output << '\n';
          throw std::runtime_error("Unexpected parser result");
        }
        CHECK(text == saved);
        ++checks;
      }
      ++cases;
    };

    expect("unsigned zero", std::string(1000, '0'), true, 0);
    expect("positive zero", "+" + std::string(999, '0'), true, 0);
    expect("negative zero", "-" + std::string(999, '0'), true, 0);
    expect("unsigned maximum", std::string(990, '0') + "2147483647", true, MAX_VALUE);
    expect("explicit positive maximum", "+" + std::string(989, '0') + "2147483647",
           true, MAX_VALUE);
    expect("negative minimum", "-" + std::string(989, '0') + "2147483648", true, MIN_VALUE);
    expect("unsigned overflow by one", std::string(990, '0') + "2147483648", false);
    expect("positive overflow by one", "+" + std::string(989, '0') + "2147483648", false);
    expect("negative overflow by one", "-" + std::string(989, '0') + "2147483649", false);
    expect("unsigned long overflow", std::string(1000, '9'), false);
    expect("positive long overflow", "+" + std::string(999, '9'), false);
    expect("negative long overflow", "-" + std::string(999, '9'), false);
    expect("invalid final letter", std::string(999, '0') + "x", false);
    expect("invalid final space", "-" + std::string(998, '0') + " ", false);

    std::string embeddedNull(1000, '0');
    embeddedNull.back() = '\0';
    expect("invalid final null byte", embeddedNull, false);

    std::string nonAscii(1000, '0');
    nonAscii.front() = '+';
    nonAscii.back() = static_cast<char>(0x80);
    expect("invalid final non-ASCII byte", nonAscii, false);

    std::cout << "B1 boundary tests passed (" << cases << " strings, 1000 bytes each, "
              << checks << " output checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
