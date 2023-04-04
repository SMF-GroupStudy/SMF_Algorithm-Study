package jiggy.lv0;

import java.util.Scanner;

public class ice_americano {
    public static int value = 5500;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int money = sc.nextInt();
        solution(money);
    }

    private static void solution(int money) {
        int count = money / value;
        int change = money - (count * value);

        int[] answer = {count, change};
        System.out.println("[" + answer[0] + ", " + answer[1] + "]");
    }
}
