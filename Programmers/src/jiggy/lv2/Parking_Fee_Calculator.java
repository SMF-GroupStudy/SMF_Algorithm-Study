package jiggy.lv2;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class Parking_Fee_Calculator {
    public static void main(String[] args) {
        int[] fees = {180, 5000, 10, 600};
        String[] records = {"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};
        int[] result = solution(fees, records);
        System.out.println(Arrays.toString(result));
    }

    public static int[] solution(int[] fees, String[] records) {

        int std_time = fees[0];
        int std_pay = fees[1];
        int per_time = fees[2];
        int per_pay = fees[3];

        // key = 차량 넘버, value = 입장 시간
        Map<Integer, Integer> map = new HashMap<>();
        // key = 차량 넘버, value = 이용비
        Map<Integer, Integer> result = new TreeMap<>();

        // 주차기록 처리하기
        for (String data : records) {
            String[] temp = data.split(" ");
            int time = cal_time(temp[0]);
            int car_num = Integer.parseInt(temp[1]);
            String state = temp[2];

            if (state.equals("OUT")) {
                int start = map.get(car_num);
                int use_time = time - start;
                if (result.containsKey(car_num)) {
                    int a = result.get(car_num);
                    use_time += a;
                }
                result.put(car_num, use_time);
                map.remove(car_num);
                continue;
            }
            map.put(car_num, time);
        }

        // 아직 안나간 차량 처리
        for (int num : map.keySet()) {
            Integer d = map.get(num);
            d = d == null ? 0 : d;

            int start = d;
            int use_time = 1439 - start;

            Integer e = result.get(num);
            e = e == null ? 0 : e;

            result.put(num, use_time + e);
        }

        // 출력하기
        int[] answer = new int[result.size()];
        int i = 0;
        for (int data : result.keySet()) {
            int time = result.get(data);

            if (time <= std_time) {
                time = std_pay;
            } else {
                time = std_pay + (int) Math.ceil((double) (time - std_time) / per_time) * per_pay;
            }
            answer[i] = time;
            i++;
        }

        return answer;
    }

    public static int cal_time(String time) {
        String[] temp = time.split(":");
        int hour = Integer.parseInt(temp[0]) * 60;
        int min = Integer.parseInt(temp[1]);
        return hour + min;
    }
}
