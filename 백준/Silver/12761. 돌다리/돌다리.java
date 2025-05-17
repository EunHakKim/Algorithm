
import java.io.*;
import java.util.*;

public class Main {
    public static int n, m, a, b;
    public static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new int[100001];
        visited[n] = 1;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);

        while (!queue.isEmpty()) {
            int next = queue.poll();

            // 앞으로 +1
            if (next + 1 < 100001) {
                if (visited[next + 1] == 0) {
                    visited[next + 1] = visited[next] + 1;
                    queue.add(next + 1);
                }
            }

            // 뒤로 -1
            if (next - 1 >= 0) {
                if (visited[next - 1] == 0) {
                    visited[next - 1] = visited[next] + 1;
                    queue.add(next - 1);
                }
            }

            // 앞으로 +a
            if (next + a < 100001) {
                if (visited[next + a] == 0) {
                    visited[next + a] = visited[next] + 1;
                    queue.add(next + a);
                }
            }


            // 뒤로 -a
            if (next - a >= 0) {
                if (visited[next - a] == 0) {
                    visited[next - a] = visited[next] + 1;
                    queue.add(next - a);
                }
            }

            // 앞으로 +b
            if (next + b < 100001) {
                if (visited[next + b] == 0) {
                    visited[next + b] = visited[next] + 1;
                    queue.add(next + b);
                }
            }

            // 뒤로 -b
            if (next - b >= 0) {
                if (visited[next - b] == 0) {
                    visited[next - b] = visited[next] + 1;
                    queue.add(next - b);
                }
            }

            // a배 이동
            if (next * a >= 0 && next * a < 100001) {
                if (visited[next * a] == 0) {
                    visited[next * a] = visited[next] + 1;
                    queue.add(next * a);
                }
            }

            // b배 이동
            if (next * b >= 0 && next * b < 100001) {
                if (visited[next * b] == 0) {
                    visited[next * b] = visited[next] + 1;
                    queue.add(next * b);
                }
            }
        }
        System.out.println(visited[m] - 1);
    }
}
