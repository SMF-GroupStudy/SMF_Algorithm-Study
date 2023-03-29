package jiggy.basic;

import java.util.Scanner;

public class Print_Right_Triangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 2중 for문을 통한 문제풀이
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // repeat() 메소드를 사용해 for문을 1번만 사용
        for (int i = 1; i <= n; i++) {
            System.out.println("*".repeat(i));
        }
    }
}
