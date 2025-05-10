import java.awt.*;
import java.io.*;
import java.util.*;

public class Main {
    public static int n, m;
    public static int[][] miro;
    public static int[][] visited;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};
    public static Queue<Point> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        miro = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                miro[i][j] = s.charAt(j) - '0';
                visited[i][j] = -1;
            }
        }

        visited[0][0] = 1;
        queue = new LinkedList<>();
        queue.offer(new Point(0, 0));
        while (!queue.isEmpty()) {
            Point cp = queue.poll();
            for (int k = 0; k < 4; k++) {
                int nx = cp.x + dx[k];
                int ny = cp.y + dy[k];
                if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                    if (miro[ny][nx] == 1 && visited[ny][nx] == -1) {
                        visited[ny][nx] = visited[cp.y][cp.x] + 1;
                        queue.offer(new Point(nx, ny));
                    }
                }
            }
        }
        System.out.println(visited[n - 1][m - 1]);
    }
}