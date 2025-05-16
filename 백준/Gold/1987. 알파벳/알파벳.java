
import java.io.*;
import java.util.*;

public class Main {
    public static int r, c, ans;
    public static char[][] graph;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        ans = 0;
        graph = new char[r][c];

        for (int i = 0; i < r; i++) {
            String str = br.readLine();
            for (int j = 0; j < c; j++) {
                graph[i][j] = str.charAt(j);
            }
        }

        Set<String> set = new HashSet<>();
        set.add(String.valueOf(graph[0][0]));
        back(0, 0, set, 1);
        System.out.println(ans);
    }

    public static void back(int cx, int cy, Set<String> set, int depth) {
        ans = Math.max(ans, depth);

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if (0 <= nx && nx < c && 0 <= ny && ny < r) {
                if (!set.contains(String.valueOf(graph[ny][nx]))) {
                    set.add(String.valueOf(graph[ny][nx]));
                    back(nx, ny, set, depth + 1);
                    set.remove(String.valueOf(graph[ny][nx]));
                }
            }
        }
    }
}