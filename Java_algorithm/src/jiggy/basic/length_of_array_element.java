package jiggy.basic;

import java.util.Arrays;

public class length_of_array_element {
    public static void main(String[] args) {
        String[] strlist = {"We", "are", "the", "world!"};
        System.out.println(Arrays.toString(solution(strlist)));
    }

    public static int[] solution(String[] strlist) {
        int length = strlist.length;
        int[] answer = new int[length];
        for (int i = 0; i < length; i++) {
            answer[i] = strlist[i].length();
        }

        return answer;
    }
}
