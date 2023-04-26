package jiggy.lv2;

import java.util.Arrays;

public class Repeat_Binary_Conversion {
    public static void main(String[] args) {
        String s = "110010101001";
        System.out.println(Arrays.toString(solution(s)));
    }

    public static int[] solution(String s) {
        int zero = 0;
        int count = 0;
        while (true) {
            count++;
            int sl = s.length();
            s = s.replace("0", "");
            zero += sl - s.length();
            if (s.equals("1")) break;
            s = Integer.toBinaryString(s.length());
        }
        return new int[]{count, zero};
    }
}
