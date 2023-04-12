package jiggy.lv2;

public class representation_of_numbers {
    public static void main(String[] args) {
        System.out.println(solution(solution(15)));
    }

    private static int solution(int n) {
        int answer = 1;

        for (int i = 1; i < n / 2 + 1; i++) {
            int sum = 0;
            for (int j = i; j <= n / 2 + 1; j++) {
                sum += j;
                if (sum == n) {
                    answer++;
                    break;
                } else if (sum > n) {
                    break;
                }
            }
        }

        return answer;
    }
}
