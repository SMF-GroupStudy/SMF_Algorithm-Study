package jiggy.lv2;

public class N_Least_Common_Multiples {
    public static void main(String[] args) {
        int[] arr = {2, 6, 8, 14};
        int result = solution(arr);
        System.out.println("result = " + result);
    }

    public static int solution(int[] arr) {
        int answer = 1;
        for (int i : arr) {
            int max = GCD(answer, i);
            answer = (i * answer) / max;
        }

        return answer;
    }

    private static int GCD(int num1, int num2) {
        if (num1 % num2 == 0)
            return num2;
        return GCD(num2, num1 % num2);
    }
}
