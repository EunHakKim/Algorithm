import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static int M, N, H;
    public static StringTokenizer st;
    public static int[][][] graph;
    public static boolean[][][] visited;
    public static Queue<Node> queue;
    public static int[] dx={0,0,1,0,-1,0};
    public static int[] dy={0,0,0,-1,0,1};
    public static int[] dz={1,-1,0,0,0,0};
    public static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        graph = new int[101][101][101];
        visited = new boolean[101][101][101];

        for(int k=0;k<H;k++) {
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < M; j++) {
                    graph[k][i][j]=Integer.parseInt(st.nextToken());
                }
            }
        }

        bfs();
        result=0;
        for(int k=0;k<H;k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if(graph[k][i][j]==0){
                        System.out.println(-1);
                        return;
                    }
                    result=Math.max(result, graph[k][i][j]-1);
                }
            }
        }
        System.out.println(result);
    }

    public static class Node{
        int x;
        int y;
        int z;

        public Node(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

    public static void bfs(){
        queue = new LinkedList<>();
        for(int k=0;k<H;k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if(graph[k][i][j]==1){
                        visited[k][i][j]=true;
                        queue.offer(new Node(j,i,k));
                    }
                }
            }
        }

        while (!queue.isEmpty()) {
            Node temp = queue.poll();
            for(int k=0;k<6;k++){
                int nx = temp.x + dx[k];
                int ny = temp.y + dy[k];
                int nz = temp.z + dz[k];

                if(0<=nx && nx<M && 0<=ny && ny<N && 0<=nz && nz<H){
                    if(graph[nz][ny][nx]==0 && !visited[nz][ny][nx]){
                        visited[nz][ny][nx]=true;
                        graph[nz][ny][nx]=graph[temp.z][temp.y][temp.x]+1;
                        queue.offer(new Node(nx,ny,nz));
                    }
                }
            }
        }
    }
}