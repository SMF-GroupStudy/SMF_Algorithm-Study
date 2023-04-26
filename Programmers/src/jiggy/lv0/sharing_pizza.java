package jiggy.lv0;

import java.util.Scanner;

public class sharing_pizza {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(solution(n));
    }

    public static int solution(int n) {
        if (n % 7 == 0)
            return n / 7;
        return (n / 7) + 1;
    }
}
