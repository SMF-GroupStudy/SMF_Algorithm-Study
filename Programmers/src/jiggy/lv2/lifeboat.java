package jiggy.lv2;

import java.util.Arrays;


public class lifeboat {
    public static void main(String[] args) {
        int[] people = {70, 80, 50};
        int limit = 100;
        System.out.println(solution(people, limit));
    }

    public static int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int max_idx = people.length - 1;
        int min_idx = 0;
        while (min_idx <= max_idx) {
            if (people[max_idx] + people[min_idx] <= limit) min_idx++;
            answer++;
            max_idx--;
        }
        return answer;
    }
}
