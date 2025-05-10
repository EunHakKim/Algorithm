
import java.io.*;
import java.util.*;

public class Main {
    public static int n, m, v;
    public static int[][] graph;
    public static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        dfs(v);
        System.out.println();
        for (int i = 0; i < n + 1; i++) {
            visited[i] = false;
        }
        bfs();
    }

    public static void dfs(int cx) {
        visited[cx] = true;
        System.out.print(cx);
        System.out.print(" ");

        for (int i = 1; i < n + 1; i++) {
            if (graph[cx][i] == 1 && ! visited[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(v);
        visited[v] = true;
        while (!queue.isEmpty()) {
            int nx = queue.poll();
            System.out.print(nx);
            System.out.print(" ");
            for (int i = 1; i < n + 1; i++) {
                if (graph[nx][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue.offer(i);
                }
            }
        }
    }
}
