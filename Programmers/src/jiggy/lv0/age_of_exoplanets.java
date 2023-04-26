package jiggy.lv0;

public class age_of_exoplanets {
    public static void main(String[] args) {
        System.out.println(solution(250));
        System.out.println(solution2(250));
        System.out.println(solution3(250));
    }

    public static String solution(int age) {
        if (age == 1000) return "baaa";
        if (age >= 100) {
            char hundreds = (char) (age / 100 + 97);
            age %= 100;
            char tens = (char) (age / 10 + 97);
            char ones = (char) (age % 10 + 97);
            return String.valueOf(new char[]{hundreds, tens, ones});
        } else if (age >= 10) {
            char tens = (char) (age / 10 + 97);
            char ones = (char) (age % 10 + 97);
            return String.valueOf(new char[]{tens, ones});
        } else return String.valueOf((char) (age + 97));
    }

    public static String solution2(int age) {
        StringBuilder answer = new StringBuilder();
        String s = String.valueOf(age);
        String[] arr = s.split("");

        for (String value : arr) {
            answer.append((char) ((Integer.parseInt(value)) + 97));
        }

        return answer.toString();
    }

    public static String solution3(int age) {
        StringBuilder answer = new StringBuilder();
        String[] alpha = new String[]{"a","b","c","d","e","f","g","h","i","j"};

        while(age>0){
            answer.insert(0, alpha[age % 10]);
            age /= 10;
        }

        return answer.toString();
    }
}
