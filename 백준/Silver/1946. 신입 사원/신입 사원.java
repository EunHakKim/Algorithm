
import java.io.*;
import java.util.*;

public class Main {
    public static int t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[n];
            int ans = 1;
            StringTokenizer st;

            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                arr[a - 1] = b;
            }

            int top = arr[0];
            for (int j = 1; j < n; j++) {
                if (arr[j] < top) {
                    ans += 1;
                    top = arr[j];
                }
            }
            System.out.println(ans);
        }
    }
}
