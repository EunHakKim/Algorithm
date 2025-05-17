
import java.io.*;
import java.util.*;

public class Main {
    public static int n, k;
    public static long ans;
    public static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        k = Integer.parseInt(br.readLine());
        ans = 0;

        for (int i = 0; i < n; i++) {
            long sum = 0;
            int j = i;
            while (j < n) {
                sum += nums[j];
                if (sum > k) {
                    ans += n - j;
                    break;
                } else {
                    j ++;
                }
            }
        }
        System.out.println(ans);
    }
}