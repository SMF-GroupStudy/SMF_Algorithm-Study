package jiggy.lv2;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class English_ending {
    public static void main(String[] args) {
        String[] words = {"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"};
        int n = 3;
        System.out.println(Arrays.toString(solution(n, words)));
    }

    public static int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        Set<String> set = new HashSet<>();
        set.add(words[0]);
        char last = words[0].charAt(words[0].length() - 1);

        for (int i = 1; i < words.length; i++) {
            String word = words[i];
            char first = word.charAt(0);

            if (last != first || set.contains(word)) {
                answer[0] = (i % n) + 1;
                answer[1] = (i / n) + 1;
                break;
            }

            set.add(word);
            last = word.charAt(word.length() - 1);
        }
        return answer;
    }
}
