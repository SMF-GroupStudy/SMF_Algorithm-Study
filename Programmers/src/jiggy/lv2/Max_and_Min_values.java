package jiggy.lv2;

import java.util.Arrays;
import java.util.stream.Stream;

public class Max_and_Min_values {

    public static void main(String[] args) {
        String s = "-1 -2 -3 -4";
        System.out.println(solution(s));
    }

    private static String solution(String s) {
        String answer;
        int[] array = Stream.of(s.split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(array);

        answer = array[0] + " " + array[array.length - 1];
        return answer;
    }
}
