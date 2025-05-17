
import java.io.*;
import java.util.*;

public class Main {
    public static int n, m, ans;
    public static Set<Integer> set;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        set = new HashSet<>();
        ans = Math.abs(n - 100);
        for (int i = 0; i < 10; i++) {
            set.add(i);
        }

        if (m != 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                set.remove(Integer.parseInt(st.nextToken()));
            }
        }

        for (int i = 0; i < 999999; i++) {
            if (check(i)) {
                int min = Math.abs(n - i) + String.valueOf(i).length();
                ans = Math.min(min, ans);
            }
        }
        System.out.println(ans);
    }

    public static boolean check(Integer value) {
        String str = String.valueOf(value);
        for (int i = 0; i < str.length(); i++) {
            if (!set.contains(str.charAt(i) - '0')) {
                return false;
            }
        }
        return true;
    }
}