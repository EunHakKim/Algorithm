
import java.io.*;
import java.util.*;

public class Main {
    public static int n, l, r, x, ans;
    public static int[] a;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        ans = 0;

        a = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);

        back(-1, -1, 0, 0);
        System.out.println(ans);
    }

    public static void back(int last, int first, int sum, int depth) {
        if (l <= sum && sum <= r && depth >= 2) {
            if (a[last] - a[first] >= x) {
                ans ++;
            }
        } else if (sum > r) {
            return;
        }

        for (int i = last + 1; i < n; i++) {
            if (first == -1) {
                back(i, i, a[i], depth + 1);
            } else {
                back(i, first, sum + a[i], depth + 1);
            }
        }
    }
}