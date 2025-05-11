import java.io.*;
import java.util.*;

public class Main {
    public static int n, ans;
    public static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        queue = new LinkedList<>();
        ans = 0;

        for (int i = 1; i < n + 1; i++) {
            queue.offer(i);
        }

        while (!queue.isEmpty()) {
            ans = queue.poll();

            if (queue.isEmpty()) {
                break;
            }

            int temp = queue.poll();
            queue.offer(temp);
        }
        System.out.println(ans);
    }
}