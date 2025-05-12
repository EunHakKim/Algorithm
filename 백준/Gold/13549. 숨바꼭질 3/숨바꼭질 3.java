
import java.io.*;
import java.util.*;

public class Main {
    public static int n, k;
    public static int[] visited;
    public static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        visited = new int[200000];
        for (int i = 0; i < 200000; i++) {
            visited[i] = -1;
        }

        bfs();
        System.out.println(visited[k]);
    }

    public static void bfs() {
        queue = new LinkedList<>();
        addQueue(n, 0);

        while (!queue.isEmpty()) {
            int nx = queue.poll();

            if (nx + 1 < 200000) {
                if (visited[nx + 1] == -1) {
                    addQueue(nx + 1, visited[nx] + 1);
                }
            }

            if (nx - 1 >= 0) {
                if (visited[nx - 1] == -1) {
                    addQueue(nx - 1, visited[nx] + 1);
                }
            }
        }
    }

    public static void addQueue(int x, int depth) {
        while (x < 200000 && visited[x] == -1) {
            visited[x] = depth;
            queue.add(x);
            x *= 2;
        }
    }
}