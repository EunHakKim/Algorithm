
import java.util.*;
import java.io.*;

public class Main {
    public static int n;
    public static PriorityQueue<Long> heap;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        heap = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            long op = Long.parseLong(br.readLine());
            if (op == 0) {
                System.out.println(heap.isEmpty() ? 0 : heap.poll());
            } else {
                heap.offer(op);
            }
        }
    }
}