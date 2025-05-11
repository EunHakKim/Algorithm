import java.io.*;
import java.util.*;

public class Main {
    public static int n, m, left, right, ans, sumValue;
    public static int[] a;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        a = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        left = 0;
        right = 0;
        ans = 0;
        sumValue = a[0];

        while (true) {
            if (sumValue == m) {
                ans ++;
                right ++;
                if (right >= n) break;
                sumValue += a[right];
            } else if (sumValue > m) {
                sumValue -= a[left];
                left ++;
            } else {
                right ++;
                if (right >= n) break;
                sumValue += a[right];
            }
        }

        System.out.println(ans);
    }
}