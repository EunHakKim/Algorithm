
import java.util.*;
import java.io.*;

public class Main {
    public static int t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int[] a = new int[n];
            int[] b = new int[m];

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                a[j] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                b[j] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(b);
            int ans = 0;

            for (int j = 0; j < n; j++) {
                int start = 0, end = m - 1;

                while (start < end) {
                    int mid = (start + end) / 2;

                    if (a[j] > b[mid]) {
                        start = mid + 1;
                    } else {
                        end = mid;
                    }
                }
                if (a[j] > b[start]) {
                    ans += start + 1;
                } else {
                    ans += start;
                }
            }
            System.out.println(ans);
        }
    }
}