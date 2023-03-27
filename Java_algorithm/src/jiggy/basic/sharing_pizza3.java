package jiggy.basic;

import java.util.Scanner;

public class sharing_pizza3 {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int slice = sc.nextInt();
        int n = sc.nextInt();
        System.out.println(solution(slice, n));
    }

    public static int solution(int slice, int n) {
        int answer = n / slice;
        if (n % slice == 0)
            return answer;
        return answer + 1;
    }
}
