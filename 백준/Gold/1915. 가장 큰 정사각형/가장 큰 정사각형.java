import java.io.*;
import java.util.*;

public class Main {
    public static int n, m, ans;
    public static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        ans = 0;

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = str.charAt(j) - '0';
                if (ans == 0 && arr[i][j] == 1) {
                    ans = 1;
                }
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (arr[i][j] == 1) {
                    int temp = Math.min(arr[i - 1][j], arr[i][j - 1]);
                    arr[i][j] = Math.min(temp, arr[i - 1][j - 1]) + 1;
                    ans = Math.max(ans, arr[i][j]);
                }
            }
        }

        System.out.println(ans * ans);
    }
}