package jiggy.lv2;

public class expected_bracket {
    public static void main(String[] args) {
        int n = 8, a = 4, b = 7;
        System.out.println(solution(n, a, b));
    }

    public static int solution(int n, int a, int b)
    {
        int answer = 1;
        while ((a + 1) / 2 != (b + 1) / 2) {
            answer++;
            a = (a + 1) / 2;
            b = (b + 1) / 2;
        }
        return answer;
    }
}
