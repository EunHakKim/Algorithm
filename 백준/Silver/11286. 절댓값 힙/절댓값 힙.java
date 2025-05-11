import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Long> heap = new PriorityQueue<>((a, b) -> {
            if (Math.abs(a) == Math.abs(b)) return Long.compare(a, b);
            return Long.compare(Math.abs(a), Math.abs(b));
        });

        for (int i = 0; i < n; i++) {
            long x = Long.parseLong(br.readLine());
            if (x == 0) {
                System.out.println(heap.isEmpty() ? 0 : heap.poll());
            } else {
                heap.offer(x);
            }
        }
    }
}