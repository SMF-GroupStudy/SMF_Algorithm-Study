package jiggy.lv2;

public class String_Compression {
    public int solution(String s) {
        int answer = s.length();
        for (int i = 1; i <= s.length() / 2; i++) {
            StringBuilder compressed = new StringBuilder();
            String pattern = s.substring(0, i);
            int count = 1;
            for (int j = i; j <= s.length() - i; j += i) {
                String substring = s.substring(j, j + i);
                if (pattern.equals(substring)) {
                    count++;
                } else {
                    if (count > 1) {
                        compressed.append(count).append(pattern);
                    } else {
                        compressed.append(pattern);
                    }
                    pattern = substring;
                    count = 1;
                }
            }
            if (count > 1) {
                compressed.append(count).append(pattern);
            } else {
                compressed.append(pattern);
            }
            compressed.append(s.substring(s.length() - s.length() % i));
            answer = Math.min(answer, compressed.length());
        }
        return answer;
    }


}
