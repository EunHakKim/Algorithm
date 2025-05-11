
import java.io.*;
import java.util.*;

public class Main {
    public static int n, ans;
    public static int[] fruits;
    public static HashMap<Integer, Integer> map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        fruits = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            fruits[i] = Integer.parseInt(st.nextToken());
        }
        map = new HashMap<>();
        map.put(fruits[0], 1);
        int left = 0, right = 0;
        ans = 0;

        while (true) {
            if (map.size() <= 2) {
                ans = Math.max(ans, right - left + 1);
                right ++;
                if (right >= n) break;
                map.put(fruits[right], map.getOrDefault(fruits[right], 0) + 1);
            } else {
                while (true) {
                    int temp = map.get(fruits[left]) - 1;
                    if (temp == 0) {
                        map.remove(fruits[left]);
                        left ++;
                        break;
                    }
                    map.put(fruits[left], temp);
                    left ++;
                }
            }
        }
        System.out.println(ans);
    }
}