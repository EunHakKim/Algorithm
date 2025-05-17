
import java.util.*;
import java.io.*;

public class Main {
    public static int n, k, ans;
    public static int[] s;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        s = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            s[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int temp = 0;
        if (s[0] % 2 != 0) temp ++;

        while (true) {
            if (temp > k) {
                while (temp > k) {
                    if (s[left] % 2 != 0) temp --;
                    left ++;
                }
            } else {
                ans = Math.max(ans, right - left + 1 - temp);
                right ++;
                if (right >= n) break;
                if (s[right] % 2 != 0) temp ++;
            }
        }
        System.out.println(ans);
    }
}
