package jiggy.lv2;

import java.util.*;

public class Picking_Tangerines {
    public static void main(String[] args) {
        int k = 6;
        int[] tangerine = {1, 3, 2, 5, 4, 5, 2, 3};
        int result = solution(k, tangerine);
        System.out.println("result = " + result);
    }

    private static int solution(int k, int[] tangerine) {
        int answer = 0;

        // 크기별로 몇 개 있는지 map에 저장함
        Map<Integer, Integer> map = new HashMap<>();
        for (int tan : tangerine) {
            map.put(tan, map.getOrDefault(tan, 0) + 1);
        }

        // 개수(value)가 많은 순으로 정렬
        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(map.entrySet());
        entryList.sort(((o1, o2) -> o2.getValue().compareTo(o1.getValue())));

        // 개수가 많은 순부터 사용
        for (Map.Entry<Integer, Integer> entry : entryList) {
            if (k <= 0) break;
            answer++;
            k -= entry.getValue();
        }

        return answer;
    }
}
