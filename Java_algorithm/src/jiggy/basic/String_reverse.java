package jiggy.basic;

import java.util.Scanner;

public class String_reverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String my_string = sc.next();
        System.out.println(solution(my_string));
    }

    public static String solution(String my_string) {
        int length = my_string.length();
        StringBuilder answer = new StringBuilder();
        for (int i = length - 1; i >= 0; i--) {
            answer.append(my_string.charAt(i));
        }
        return answer.toString();
    }
}
