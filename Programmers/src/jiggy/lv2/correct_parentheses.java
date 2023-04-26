package jiggy.lv2;

public class correct_parentheses {
    public static void main(String[] args) {
        String parentheses = "(())()";
        System.out.println(solution(parentheses));
        System.out.println(solution2(parentheses));
    }

    private static boolean solution2(String parentheses) {
        boolean answer = true;
        int count = 0;

        for (int i = 0; i < parentheses.length(); i++) {
            if (parentheses.charAt(i) == '(') count++;
            else count--;

            if (count < 0) answer = false;
        }
        if (count != 0) answer = false;

        return answer;
    }

    private static boolean solution(String parentheses) {
        boolean answer = true;
        int count = 0;
        for (String par: parentheses.split("")) {
            count += par.equals("(") ? 1 : -1;
            if (count < 0) return false;
        }
        if (count!=0) answer = false;
        return answer;
    }
}
