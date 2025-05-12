
import java.util.*;
import java.io.*;

public class Main {
    public static int n, k;
    public static int[] coins;
    public static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        coins = new int[n];
        dp = new int[k + 1];

        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        for (int j = 0; j < k + 1; j++) {
            dp[j] = -1;
        }

        for (int i = 0; i < n; i++) {
            if (coins[i] >= k + 1) continue;
            dp[coins[i]] = 1;
            for (int j = 0; j < k + 1; j++) {
                if (j + coins[i] < k + 1 && dp[j] != -1) {
                    if (dp[j + coins[i]] == -1) {
                        dp[j + coins[i]] = dp[j] + 1;
                    } else {
                        dp[j + coins[i]] = Math.min(dp[j + coins[i]], dp[j] + 1);
                    }
                }
            }
        }
        System.out.println(dp[k]);
    }
}
