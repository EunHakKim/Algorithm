
import java.io.*;
import java.util.*;

public class Main {
    public static int n, k;
    public static int[] levels;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        levels = new int[n];

        for (int i = 0; i < n; i++) {
            levels[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(levels);

        long ans = 0;
        long left = 0;
        long right = 2000000000;

        while (left <= right) {
            long mid = (left + right) / 2;
            long sum = 0;

            for (int i = 0; i < n; i++) {
                if (levels[i] >= mid) break;
                sum += (mid - levels[i]);
            }

            if (sum > k){
                right = mid - 1;
            } else {
                ans = mid;
                left = mid + 1;
            }
        }
        System.out.println(ans);
    }
}