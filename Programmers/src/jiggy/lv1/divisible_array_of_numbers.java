package jiggy.lv1;

import java.util.ArrayList;
import java.util.Arrays;

public class divisible_array_of_numbers {
    public static void main(String[] args) {
        int[] arr = {5, 9, 7, 10};
        int divisor = 5;
        System.out.println((Arrays.toString(solution(arr, divisor))));
    }

    private static int[] solution(int[] arr, int divisor) {
        int[] answer;
        ArrayList<Integer> arr2 = new ArrayList<>();
        for (int i : arr) {
            if (i % divisor == 0) {
                arr2.add(i);
            }
        }
        answer = arr2.stream().mapToInt(i -> i).toArray();
        if (answer.length == 0) answer = new int[] {-1};

        return answer;
    }
}
