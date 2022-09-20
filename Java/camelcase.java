class Solution {
  public static String camelCase(String input) {
    String s = "";
    for (int i = 0; i<input.length(); i++) {
      if (Character.isUpperCase(input.charAt(i))) {
        s += " " + input.charAt(i);
      } else {
        s += input.charAt(i) + "";
      }
    }
    return s;
  }
}
