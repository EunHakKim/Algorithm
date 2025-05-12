import java.awt.*;
import java.io.*;
import java.util.*;

public class Main {
    public static int r, c;
    public static char[][] miro;
    public static int[][] visited;
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};
    public static Queue<Point> jihun;
    public static Queue<Point> fires;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        miro = new char[r][c];
        visited = new int[r][c];

        fires = new LinkedList<>();
        jihun = new LinkedList<>();

        for (int i = 0; i < r; i++) {
            String str = br.readLine();
            for (int j = 0; j < c; j++) {
                visited[i][j] = -1;
                miro[i][j] = str.charAt(j);

                if (miro[i][j] == 'J') {
                    jihun.add(new Point(j, i));
                    visited[i][j] = 0;
                    miro[i][j] = '.';
                } else if(miro[i][j] == 'F') {
                    fires.add(new Point(j, i));
                }
            }
        }

        while (!jihun.isEmpty()) {
            // 불 이동
            int fireSize = fires.size();
            for (int i = 0; i < fireSize; i++) {
                Point cf = fires.poll();
                for (int k = 0; k < 4; k++) {
                    int nx = cf.x + dx[k];
                    int ny = cf.y + dy[k];
                    if (0 <= nx && nx < c && 0 <= ny && ny < r) {
                        if (miro[ny][nx] == '.') {
                            miro[ny][nx] = 'F';
                            fires.add(new Point(nx, ny));
                        }
                    }
                }
            }

            // 지훈 이동
            int jihunSize = jihun.size();
            for (int i = 0; i < jihunSize; i++) {
                Point cj = jihun.poll();
                // 탈출 검사
                if (cj.x == 0 || cj.x == c - 1 || cj.y == 0 || cj.y == r - 1) {
                    System.out.println(visited[cj.y][cj.x] + 1);
                    return;
                }

                for (int k = 0; k < 4; k++) {
                    int nx = cj.x + dx[k];
                    int ny = cj.y + dy[k];
                    if (0 <= nx && nx < c && 0 <= ny && ny < r) {
                        if (miro[ny][nx] == '.' && visited[ny][nx] == -1) {
                            visited[ny][nx] = visited[cj.y][cj.x] + 1;
                            jihun.add(new Point(nx, ny));
                        }
                    }
                }
            }
        }
        System.out.println("IMPOSSIBLE");
    }
}
