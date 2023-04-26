package jiggy.lv2;

import java.util.Arrays;

public class carpet {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(8, 1)));
    }

    public static int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int x;
        int y;
        for (int i = 1; i < yellow + 1; i++) {
            if (yellow % i == 0) {
                x = yellow / i;
                y = i;
                int brown_tmp = (x * 2) + (y * 2) + 4;
                if (brown_tmp == brown) {
                    answer[0] = x + 2;
                    answer[1] = y + 2;
                    return answer;
                }
            }
        }

        return answer;
    }
}
