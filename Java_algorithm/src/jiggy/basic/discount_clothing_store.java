package jiggy.basic;

import java.util.Scanner;

public class discount_clothing_store {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int price = sc.nextInt();
        System.out.println(solution(price));
    }

    public static int solution(int price) {
        if (price >= 100000 && price < 300000) {
            return calculate(price, 5);
        } else if (price >= 300000 && price < 500000) {
            return calculate(price, 10);
        } else if (price >= 500000) {
            return calculate(price, 20);
        }

        return price;
    }

    public static int calculate(int price, float discount_rate) {
        return (int) (price - (price * (discount_rate / 100)));
    }
}
