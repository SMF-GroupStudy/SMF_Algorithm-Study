package jiggy.lv0;

import java.util.Arrays;
import java.util.stream.IntStream;

public class slice_to_array {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(useCopyOfRange(new int[]{1, 2, 3, 4, 5}, 1, 3)));
        System.out.println(Arrays.toString(useStream(new int[]{1, 2, 3, 4, 5}, 1, 3)));
    }

    public static int[] useCopyOfRange(int[] numbers, int num1, int num2) {
        return Arrays.copyOfRange(numbers, num1, num2 + 1);
    }

    public static int[] useStream(int[] numbers, int num1, int num2) {
        return IntStream.range(num1, num2 + 1).map(i -> numbers[i]).toArray();
    }
}
