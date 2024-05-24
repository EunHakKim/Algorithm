import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static int n, m;
    public static StringTokenizer st;
    public static StringBuilder sb;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int cnt;
    public static List<Integer> list;
    public static int[] dx = {1,0,-1,0};
    public static int[] dy = {0,-1,0,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());

        graph = new int[501][501];
        visited = new boolean[501][501];
        list = new ArrayList<>();
        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<m;j++){
                graph[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(graph[i][j]==1 && !visited[i][j]){
                    cnt=1;
                    visited[i][j]=true;
                    dfs(j ,i);
                    list.add(cnt);
                }
            }
        }
        sb.append(list.size()).append("\n");
        if(list.isEmpty()){
            sb.append(0);
        }else{
            sb.append(Collections.max(list));
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int x, int y) {
        for(int k=0;k<4;k++){
            int nx = x+dx[k];
            int ny = y+dy[k];
            if(0<=nx && nx<m && 0<=ny && ny<n){
                if(graph[ny][nx]==1 && !visited[ny][nx]){
                    visited[ny][nx]=true;
                    cnt++;
                    dfs(nx, ny);
                }
            }
        }
    }
}