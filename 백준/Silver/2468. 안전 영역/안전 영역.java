import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static int N;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int cnt;
    public static int result;
    public static int[] dx={1,0,-1,0};
    public static int[] dy={0,-1,0,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());

        graph = new int[101][101];
        visited = new boolean[101][101];
        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int max = 0;
        for(int i[]:graph)
            for (int j:i)
                max=Math.max(max, j);

        cnt=0;
        result=0;
        for (int k=0;k<max+1;k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (graph[i][j] > k && !visited[i][j]) {
                        cnt++;
                        dfs(j,i,k);
                    }
                }
            }
            result=Math.max(result, cnt);
            cnt=0;
            for(boolean b[]:visited){
                Arrays.fill(b, false);
            }
        }
        System.out.print(result);
    }

    public static void dfs(int x, int y, int max){
        for(int k=0;k<4;k++){
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (0<=nx && nx<N && 0<=ny && ny<N){
                if(graph[ny][nx]>max && !visited[ny][nx]){
                    visited[ny][nx]=true;
                    dfs(nx, ny, max);
                }
            }
        }
    }
}