package jiggy.lv2;

public class Creating_JadenCase_strings {
    public static void main(String[] args) {
        String s = "3people unFollowed me";
        System.out.println(solution(s));
        System.out.println(solution2(s));
    }

    // 다른 사람의 풀이
    private static String solution2(String s) {
        String answer = "";
        String[] array = s.toLowerCase().split("");
        boolean flag = true;

        for (String str: array) {
            answer += flag ? str.toUpperCase() : str;
            flag = str.equals(" ");
        }

        return answer;
    }

    private static String solution(String s) {
        String answer = "";
        // 문자열 소문자로 초기화
        s = s.toLowerCase();
        String[] array = s.split("");
        // 첫 문자를 대문자로 변환하기 위한 true 값
        boolean space = true;

        for (String str: array) {
            // 배열의 값이 공백일 경우 다음 문자 대문자로 바꾸기 위한 true 값
            if (str.equals(" ")) {
                space = true;
            }
            if (space) {
                // 공백 연달아 올 경우 예외 처리
                if (str.equals(" ")) {
                    answer += " ";
                } else {
                    // 공백 뒤 첫 음절을 대문자로 변경 후 다시 false 처리
                    space = false;
                    answer += str.toUpperCase();
                }
                // 아무 해당없는 문자는 그냥 추가
            } else answer += str;
        }

        return answer;
    }
}
