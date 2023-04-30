import java.util.Scanner;

public class number_of_words_1152 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();
        String[] arr = s.trim().split(" ");
        System.out.println(arr.length);
    }
}
