import java.io.*;

public class Main {
    public static String s;
    public static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine();
        ans = 0;
        char target = s.charAt(0);

        for (int i = 1; i < s.length(); i++) {
            if (target != s.charAt(i)) {
                target = s.charAt(i);
                ans ++;
            }
        }

        System.out.println(ans / 2 + ans % 2);
    }
}
