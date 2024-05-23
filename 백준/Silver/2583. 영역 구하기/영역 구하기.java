import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static StringTokenizer st;
    public static int M, N, K;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int cnt;
    public static int[] dx={1,0,-1,0};
    public static int[] dy={0,-1,0,1};
    public static List<Integer> results;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        graph = new int[101][101];
        visited = new boolean[101][101];
        results = new ArrayList<>();

        for(int i=0;i<K;i++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            for(int k=y1;k<y2;k++) {
                for (int j = x1; j < x2; j++) {
                    graph[k][j]=1;
                }
            }
        }


        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(!(graph[i][j]==1) && !visited[i][j]){
                    cnt=1;
                    visited[i][j]=true;
                    dfs(j, i);
                    results.add(cnt);
                }
            }
        }
        Collections.sort(results);
        System.out.println(results.size());
        for(Integer i:results)
            System.out.print(i + " ");
    }

    public static void dfs(int x, int y){
        for(int k=0;k<4;k++){
            int nx = x+dx[k];
            int ny = y+dy[k];

            if(0<=nx && nx<N && 0<=ny && ny<M){
                if (!(graph[ny][nx]==1) && !visited[ny][nx]){
                    visited[ny][nx]=true;
                    cnt++;
                    dfs(nx,ny);
                }
            }
        }
    }
}