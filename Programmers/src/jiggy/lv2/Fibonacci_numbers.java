package jiggy.lv2;

public class Fibonacci_numbers {
    public static void main(String[] args) {
//        System.out.println(solution(3));
        System.out.println(fibonacci_array(14));
        System.out.println(fibonacci_recursion(14));
    }

    public static int solution(int n) {
        long[] arr = new long[n + 1];
        arr[0] = 0;
        arr[1] = 1;

        for (int i = 2; i <= n; i++) {
            arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567;
        }

        return (int) arr[n] % 1234567;
    }


    // 피보나치 수열 배열
    public static int fibonacci_array(int n) {
        long[] arr = new long[n + 1];
        arr[0] = 0;
        arr[1] = 1;

        for (int i = 2; i <= n; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }

        return (int) arr[n];
    }

    // 피보나치 수열 재귀
    public static int fibonacci_recursion(int n) {
        if (n == 1) return 1;
        else if (n == 2) return 1;
        else return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1);
    }
}
