package jiggy.basic;

public class lamb_skewers {
    public static int lamb = 12000;
    public static int juice = 2000;
    public static void main(String[] args) {
        System.out.println(solution(64, 6));
    }

    public static int solution(int n, int k) {
        int discount_juice = n / 10;
        return (lamb * n) + (juice * (k - discount_juice));
    }
}
