
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static int n, m;
    public static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[m];

        back(0);
    }

    public static void back(int depth) {
        if (depth == m) {
            for(int x : arr) {
                System.out.print(x + " ");
            }
            System.out.println();
            return;
        }

        if (depth == 0) {
            for (int i = 1; i < n + 1; i++) {
                arr[depth] = i;
                back(depth + 1);
            }
        } else {
            for (int i = arr[depth - 1] + 1; i < n + 1; i++) {
                arr[depth] = i;
                back(depth + 1);
            }
        }
    }
}