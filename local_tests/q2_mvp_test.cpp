// Reuse the implementation while keeping the template's public main intact.
#define main q2_public_main
#include "../src/main/A1_q2.cpp"
#undef main

int main()
{
  try {
    CHECK(edit_labels("cam,imu", {}) == "cam,imu");
    CHECK(edit_labels("", {}) == "");
    CHECK(edit_labels("", {{"", "cam"}}) == "cam");
    CHECK(edit_labels("cam", {{"", "imu"}}) == "cam,imu");
    CHECK(edit_labels("cam", {{"", ""}}) == "cam");
    CHECK(edit_labels("cam,cam", {{"cam", "cam"}}) == "cam,cam");
    CHECK(edit_labels("cam", {{"imu", "gyro"}}) == "cam");

    CHECK(edit_labels("cam2,cam", {{"cam", "imu"}}) == "cam2,imu");
    CHECK(edit_labels("webcam,cam", {{"cam", "imu"}}) == "webcam,imu");
    CHECK(edit_labels("a,b,a", {{"a", "x"}}) == "x,b,a");
    CHECK(edit_labels("Cam,cam", {{"cam", "imu"}}) == "Cam,imu");

    CHECK(edit_labels("a,b,c", {{"a", ""}}) == "b,c");
    CHECK(edit_labels("a,b,c", {{"b", ""}}) == "a,c");
    CHECK(edit_labels("a,b,c", {{"c", ""}}) == "a,b");
    CHECK(edit_labels("a", {{"a", ""}}) == "");
    CHECK(edit_labels("", {{"a", ""}}) == "");
    CHECK(edit_labels("a", {{"a", ""}, {"", "b"}}) == "b");
    CHECK(edit_labels("a,b,c", {{"a", "camera"}, {"b", ""}, {"c", "imu"}}) ==
          "camera,imu");
    CHECK(edit_labels("a", {{"", "a"}}) == "a,a");
    CHECK(edit_labels("a,b", {{"a", "b"}}) == "b,b");
    CHECK(edit_labels("cam_1,cam_10", {{"cam_1", "X_2"}}) == "X_2,cam_10");

    std::string original = "cam,imu";
    std::vector<LabelEdit> edits = {{"cam", "camera"}, {"imu", ""}};
    CHECK(edit_labels(original, edits) == "camera");
    CHECK(original == "cam,imu");
    CHECK(edits.size() == 2 && edits[0].from == "cam" && edits[0].to == "camera" &&
          edits[1].from == "imu" && edits[1].to.empty());

    std::string longLabel(32, 'a');
    CHECK(edit_labels(longLabel, {{longLabel, "x"}}) == "x");

    std::cout << "Q2 MVP tests passed (25 checks)\n";
  } catch (const std::exception& error) {
    std::cerr << error.what() << '\n';
    return 1;
  }
  return 0;
}
