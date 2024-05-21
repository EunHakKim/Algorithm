import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static int N;
    public static int M;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    public static Queue<Point> queue;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        graph = new int[101][101];
        visited = new boolean[101][101];

        for(int i=0;i<N;i++){
            String line = sc.next();
            for(int j = 0; j<M;j++){
                graph[i][j] = line.charAt(j) - '0';
            }
        }
        bfs(0,0);
    }

    public static void bfs(int x, int y) {
        queue = new LinkedList<>();

        queue.offer(new Point(x, y));
        while (!queue.isEmpty()){
            Point temp = queue.poll();

            for(int k=0;k<4;k++){
                int nx = temp.x + dx[k];
                int ny = temp.y + dy[k];

                if(0<=nx && nx<M && 0<=ny && ny<N){
                    if(graph[ny][nx]==1 && !visited[ny][nx]){
                        queue.offer(new Point(nx, ny));
                        visited[ny][nx]=true;
                        graph[ny][nx]=graph[temp.y][temp.x]+1;
                    }
                }
            }
        }
        System.out.println(graph[N-1][M-1]);
    }
}