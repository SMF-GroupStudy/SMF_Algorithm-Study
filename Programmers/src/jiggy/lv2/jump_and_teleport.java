package jiggy.lv2;

public class jump_and_teleport {
    public static void main(String[] args) {
        int n = 5000;
        System.out.println(solution(n));
    }

    public static int solution(int n) {
        int answer = 0;
        while (n!=0) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n -= 1;
                answer++;
            }
        }
        return answer;
    }
}
