package jiggy.basic;

import java.util.Scanner;

public class sharing_pizza2 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(solution(n) / 6);
    }

    public static int solution(int n) {
        int piece = 6;
        int max = GCD(n, piece);

        return (n * piece) / max;
    }

    public static int GCD(int num1, int num2) {
        if (num1 % num2 == 0)
            return num2;
        return GCD(num2, num1 % num2);
    }
}
