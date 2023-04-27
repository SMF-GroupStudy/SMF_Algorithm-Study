package jiggy.lv2;

import java.util.Stack;

public class Parenthesis_Rotation {
    public static void main(String[] args) {
        String s = "[](){}";
        int result = solution(s);
        System.out.println("result = " + result);
    }
    public static int solution(String s) {
        int answer = 0;
        int n = s.length();


        for (int i = 0; i < n; i++) {
            String rotated = rotate(s, i);
            if (check(rotated)) answer++;
        }


        return answer;
    }

    public static boolean check(String s) {

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if (c == ')' && top != '(' || c == '}' && top != '{' || c == ']' && top != '[') {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }


    public static String rotate(String s, int k) {
        return s.substring(k) + s.substring(0, k);
    }
}
