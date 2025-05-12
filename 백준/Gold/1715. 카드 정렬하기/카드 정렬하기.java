
import java.io.*;
import java.util.*;

public class Main {
    public static int n;
    public static long ans;
    public static PriorityQueue<Long> pq;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        ans = 0;
        pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            long card = Long.parseLong(br.readLine());
            pq.add(card);
        }

        while (pq.size() > 1) {
            long a = pq.poll();
            long b = pq.poll();

            long temp = a + b;
            ans += temp;
            pq.add(temp);
        }
        System.out.println(ans);
    }
}