package jiggy.lv0;

public class Remove_specific_characters {
    public static void main(String[] args) {
        System.out.println(solution("BCBdbe", "B"));
    }

    public static String solution(String my_string, String letter) {
        return my_string.replaceAll(letter, "");
    }
}
