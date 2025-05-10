
import java.awt.*;
import java.util.*;
import java.io.*;
import java.util.List;

public class Main {
    public static int n;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    int temp = bfs(j, i);
                    result.add(temp);
                }
            }
        }
        Collections.sort(result);
        System.out.println(result.size());
        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }

    public static int bfs(int x, int y) {
        visited[y][x] = true;
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(x, y));
        int cnt = 1;

        while (!queue.isEmpty()) {
            Point cp = queue.poll();
            for (int k = 0; k < 4; k++) {
                int nx = cp.x + dx[k];
                int ny = cp.y + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (graph[ny][nx] == 1 && !visited[ny][nx]) {
                        visited[ny][nx] = true;
                        cnt ++;
                        queue.offer(new Point(nx, ny));
                    }
                }
            }
        }

        return cnt;
    }
}
