
import java.io.*;
import java.util.*;

public class Main {
    public static int n, topIndex, ans;
    public static int[] ceil;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        ceil = new int[1001];
        ans = 0;
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            ceil[l] = h;
        }

        // 최고 높이 계산
        topIndex = 0;
        for (int i = 1; i < 1001; i++) {
            if (ceil[topIndex] < ceil[i]) {
                topIndex = i;
            }
        }

        // 왼 -> 최고 높이 계산
        int maxValue = 0;
        for (int i = 0; i < topIndex; i++) {
            if (ceil[i] > maxValue) {
                maxValue = ceil[i];
            }
            ans += maxValue;
        }
        
        // 최고 높이 더해줌
        ans += ceil[topIndex];
        
        // 오 -> 최고 높이 계산 
        maxValue = 0;
        for (int i = 1000; i > topIndex; i--) {
            if (ceil[i] > maxValue) {
                maxValue = ceil[i];
            }
            ans += maxValue;
        }
        
        System.out.println(ans);
    }
}
