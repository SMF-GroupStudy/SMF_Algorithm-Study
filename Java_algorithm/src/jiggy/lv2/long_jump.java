package jiggy.lv2;

public class long_jump {
    public static void main(String[] args) {
        int n = 100;
        long result1 = mySolution(n);
        long result2 = solution(n);
        System.out.println("result1 = " + result1);
        System.out.println("result2 = " + result2);
    }

    private static long solution(int n) {
        long answer;

        if (n == 1) {
            return 1;
        }

        long[] dp = new long[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i < n + 1; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
        }
        answer = dp[n];
        return answer;
    }

    // 내 풀이는 39부터 정답 풀이와 달리 오답이 나온다.
    // 아마 반복문이 지나치게 돌아서 오류가 발생되는 것으로 추정
    public static long mySolution(int n) {
        long answer = 1;

        for (int i = 1; i <= n / 2; i++) {
            answer += combination(n - i, i);
        }

        return answer % 1234567;
    }

    private static long combination(int num1, int num2) {
        long numerator = 1;
        long denominator = 1;

        for (int i = 0; i < num2; i++) {
            numerator *= num1 - i;
            denominator *= (i + 1);
        }

        return  numerator / denominator;
    }
}
