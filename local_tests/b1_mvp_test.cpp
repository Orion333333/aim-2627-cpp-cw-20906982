// Reuse the saved implementation and its fixed interface.
#define main b1_public_main
#include "../src/main/A1_b1.cpp"
#undef main

int main()
{
  try {
    const int MIN_VALUE = std::numeric_limits<int>::min();
    const int MAX_VALUE = std::numeric_limits<int>::max();
    int checks = 0;
    auto expect = [&checks](const char* name, const std::string& text, int initial,
                           bool expectedSuccess, int expectedValue) {
      const std::string saved = text;
      int output = initial;
      bool success = parse_i32(text, output);
      if (success != expectedSuccess || output != expectedValue) {
        std::cerr << name << ": expected " << expectedSuccess << ',' << expectedValue
                  << "; got " << success << ',' << output << '\n';
        throw std::runtime_error("Unexpected parser result");
      }
      CHECK(text == saved);
      ++checks;
    };

    expect("public valid", "-12", 9, true, -12);
    expect("public invalid", "12x", 9, false, 9);
    expect("zero", "0", 9, true, 0);
    expect("positive zero", "+0", 9, true, 0);
    expect("negative zero", "-0", 9, true, 0);
    expect("leading zeros", "00012", 9, true, 12);
    expect("positive leading zeros", "+00012", 9, true, 12);
    expect("negative leading zeros", "-00012", 9, true, -12);
    expect("maximum positive", "2147483647", 9, true, MAX_VALUE);
    expect("explicit maximum positive", "+2147483647", 9, true, MAX_VALUE);
    expect("minimum negative", "-2147483648", 9, true, MIN_VALUE);
    expect("symmetric negative", "-2147483647", 9, true, -MAX_VALUE);
    expect("positive overflow", "2147483648", 9, false, 9);
    expect("explicit positive overflow", "+2147483648", 9, false, 9);
    expect("negative overflow", "-2147483649", 9, false, 9);
    expect("leading zeros at positive limit", "0002147483647", 9, true, MAX_VALUE);
    expect("leading zeros at negative limit", "-0002147483648", 9, true, MIN_VALUE);
    expect("empty", "", 9, false, 9);
    expect("positive sign only", "+", 9, false, 9);
    expect("negative sign only", "-", 9, false, 9);
    expect("leading space", " 1", 9, false, 9);
    expect("trailing space", "1 ", 9, false, 9);
    expect("leading tab", "\t1", 9, false, 9);
    expect("trailing newline", "1\n", 9, false, 9);
    expect("decimal point", "1.0", 9, false, 9);
    expect("scientific notation", "1e3", 9, false, 9);
    expect("hexadecimal prefix", "0x10", 9, false, 9);
    expect("double positive sign", "++1", 9, false, 9);
    expect("double negative sign", "--1", 9, false, 9);
    expect("positive then negative sign", "+-1", 9, false, 9);
    expect("negative then positive sign", "-+1", 9, false, 9);
    expect("embedded sign", "1+2", 9, false, 9);
    expect("embedded null", std::string("12\0", 3), 9, false, 9);
    expect("non-ASCII byte", std::string(1, static_cast<char>(0x80)), 9, false, 9);
    expect("fullwidth digit", "\xEF\xBC\x91", 9, false, 9);
    expect("Arabic-Indic digit", "\xD9\xA1", 9, false, 9);
    expect("64-bit-sized value", "9223372036854775807", 9, false, 9);
    expect("maximum-length overflowing value", std::string(1000, '9'), 9, false, 9);
    expect("maximum-length zeros", std::string(1000, '0'), 9, true, 0);
    expect("failure preserves minimum", "2147483648", MIN_VALUE, false, MIN_VALUE);
    expect("failure preserves maximum", "7x", MAX_VALUE, false, MAX_VALUE);

    int output = 9;
    CHECK(parse_i32("-2147483648", output) && output == MIN_VALUE);
    ++checks;
    CHECK(!parse_i32("2147483648", output) && output == MIN_VALUE);
    ++checks;
    CHECK(parse_i32("-0000", output) && output == 0);
    ++checks;

    std::cout << "B1 MVP tests passed (" << checks << " checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
