package jiggy.lv0;

import java.util.Arrays;
import java.util.Collections;

public class Setting_the_order_of_treatment {
    public static void main(String[] args) {
        int[] emergency = {3, 76, 24};

        System.out.println(Arrays.toString(solution(emergency)));
        System.out.println(Arrays.toString(solution2(emergency)));
    }

    private static int[] solution(int[] emergency) {
        Integer[] array = Arrays.stream(emergency).boxed().toArray(Integer[]::new);

        Arrays.sort(array, Collections.reverseOrder());
        int[] answer = new int[emergency.length];

        for (int i = 0; i < array.length; i++) {

            for (int j = 0; j < array.length; j++) {

                if (array[i] == emergency[j]) {
                    answer[j] = i + 1;
                }

            }

        }

        return answer;
    }

    // 다른 사람의 풀이
    private static int[] solution2(int[] emergency) {
        int[] answer = new int[emergency.length];

        for (int i = 0; i < answer.length; i++) {
            if (answer[i] != 0) {
                continue;
            }

            int idx = 1;
            for(int j = 0; j < answer.length; j++) {
                if (emergency[i] < emergency[j]) {
                    idx++;
                }
            }

            answer[i] = idx;
        }
        return answer;
    }
}
