
import java.io.*;
import java.util.*;
import java.awt.*;
import java.util.List;

public class Main {
    static class Virus implements Comparable<Virus> {
        int x, y, type, time;
        Virus(int x, int y, int type, int time) {
            this.x = x;
            this.y = y;
            this.type = type;
            this.time = time;
        }
        @Override
        public int compareTo(Virus o) {
            return this.type - o.type;  // 바이러스 번호 오름차순
        }
    }
    public static int n, k, s, x, y;
    public static int[][] graph;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        graph = new int[n][n];
        List<Virus> viruses = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] != 0) {
                    viruses.add(new Virus(j, i, graph[i][j], 0));
                }
            }
        }
        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        Collections.sort(viruses);
        Queue<Virus> queue = new LinkedList<>(viruses);

        while (!queue.isEmpty()) {
            Virus v = queue.poll();
            if (v.time == s) break;

            for (int i = 0; i < 4; i++) {
                int nx = v.x + dx[i];
                int ny = v.y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (graph[ny][nx] == 0) {
                        graph[ny][nx] = v.type;
                        queue.add(new Virus(nx, ny, v.type, v.time + 1));
                    }
                }
            }
        }

        System.out.println(graph[x - 1][y - 1]);
    }
}
