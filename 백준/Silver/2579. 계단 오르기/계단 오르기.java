
import java.io.*;

public class Main {
    public static int n;
    public static int[] stairs;
    public static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        stairs = new int[n];
        dp = new int[n][3];

        for (int i = 0; i < n; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }

        dp[0][0] = 0;
        dp[0][1] = stairs[0];
        dp[0][2] = 0;

        for (int i = 1; i < n; i++) {
            dp[i][0] = Math.max(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = dp[i - 1][0] + stairs[i];
            dp[i][2] = dp[i - 1][1] + stairs[i];
        }

        System.out.println(Math.max(dp[n - 1][1], dp[n - 1][2]));
    }
}
