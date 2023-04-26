package jiggy.lv0;

public class Print_String_repeat {
    public static void main(String[] args) {
        System.out.println(solution("hello", 3));
    }

    public static String solution(String my_string, int n) {
        int length = my_string.length();
        StringBuilder answer = new StringBuilder();
        for(int i = 0; i < length; i++) {
            String tmp = String.valueOf(my_string.charAt(i));
            answer.append(tmp.repeat(n));
        }
        return String.valueOf(answer);
    }
}
