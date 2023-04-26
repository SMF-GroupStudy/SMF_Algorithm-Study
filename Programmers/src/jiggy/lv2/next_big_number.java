package jiggy.lv2;

public class next_big_number {
    public static void main(String[] args) {
        System.out.println(solution(78));
        System.out.println(solution2(78));
    }

    public static int solution(int n) {
        int cnt1 = Integer.bitCount(n);
        n++;
        while (cnt1 != Integer.bitCount(n)) {
            n++;
        }

        return n;
    }

    // 시간 초과
    public static int solution2(int n) {
        String small_binary = Integer.toBinaryString(n);
        int small_one = countChar(small_binary, '1');

        while (true) {
            n++;
            String big_binary = Integer.toBinaryString(n);
            int big_one = countChar(big_binary, '1');
            if (big_one == small_one) break;
        }

        return n;
    }

    // 일부 런타임 오류
    public static int solution3(int n) {
        int small_binary = Integer.parseInt(Integer.toBinaryString(n));
        n++;
        while (sum_digit(small_binary) != sum_digit(Integer.parseInt(Integer.toBinaryString(n)))) {
            n++;
        }

        return n;
    }

    public static int countChar(String str, char ch) {
        return (int) str.chars().filter(c -> c == ch).count();
    }

    public static int sum_digit(int n) {
        int sum = 0;
        while (n!=0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}
