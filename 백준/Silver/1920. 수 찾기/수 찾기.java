
import java.util.*;
import java.io.*;

public class Main {
    public static int n, m;
    public static int[] a;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            binarySearch(target);
        }
    }

    public static void binarySearch(int target) {
        int left = 0;
        int right = n - 1;
        while (left < right) {
            int mid = (left + right) / 2;

            if (target > a[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if (target == a[left]) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}