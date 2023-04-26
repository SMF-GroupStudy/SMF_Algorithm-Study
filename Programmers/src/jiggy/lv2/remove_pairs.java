package jiggy.lv2;

import java.util.Stack;

public class remove_pairs {
    public static void main(String[] args) {
        String s = "baabaa";
        System.out.println(solution(s));
    }

    public static int solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!stack.empty() && stack.peek() == c) {
                stack.pop();
            } else stack.push(c);
        }
        return stack.empty()? 1 : 0;
    }
}
