import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int n, m, ans;
    public static String[] s;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        ans = 0;
        s = new String[n];

        for (int i = 0; i < n; i++) {
            s[i] = br.readLine();
        }

        for (int i = 0; i < m; i++) {
            String newS = br.readLine();
            for (int j = 0; j < n; j++) {
                if (s[j].equals(newS)) {
                    ans ++;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}