package jiggy.basic;

import java.util.ArrayList;
import java.util.Arrays;

public class array_reverse {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[]{1, 2, 3})));
        System.out.println(Arrays.toString(solution2(new int[]{1, 2, 3})));
    }

    // 다른 사람의 풀이를 참조한 코드
    private static int[] solution2(int[] num_list) {
        int length = num_list.length;
        int[] answer = new int[length];

        for (int i = 0; i < length; i++) {
            answer[i] = num_list[length - 1 - i];
        }
        return answer;
    }

    // 내가 풀이한 코드
    public static int[] solution(int[] num_list) {
        ArrayList<Integer> list = new ArrayList<>();
        int length = num_list.length;

        int[] answer = new int[length];

        for (int i = length-1; i >= 0; i--) {
            list.add(num_list[i]);
        }

        for (int j = 0; j < length; j++) {
            answer[j] = list.get(j);
        }

        return answer;
    }
}
