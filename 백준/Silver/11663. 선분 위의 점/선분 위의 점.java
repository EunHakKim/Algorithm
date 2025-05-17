
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int n, m;
    public static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            int leftIdx = bs(left);
            int rightIdx = bs(right);
            //System.out.println(leftIdx + " " + rightIdx);
            int ans = rightIdx - leftIdx - 1;
            if (arr[rightIdx] <= right) ans ++;
            if (arr[leftIdx] >= left) ans ++;
            System.out.println(ans);
        }
    }

    public static int bs(int target) {
        int st = 0;
        int en = n - 1;

        while (st < en) {
            int mid = (st + en) / 2;

            if (arr[mid] < target) {
                st = mid + 1;
            } else {
                en = mid;
            }
        }
        return st;
    }
}