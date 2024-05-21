import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static int N;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int cnt;
    public static List<Integer> results;
    public static int[] dx = {1,0,-1,0};
    public static int[] dy = {0,-1,0,1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        graph = new int[26][26];
        visited = new boolean[26][26];
        results = new ArrayList<>();

        for(int i=0;i<N;i++){
            String line = sc.next();
            for (int j=0;j<N;j++){
                graph[i][j]=line.charAt(j) - '0';
            }
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(graph[i][j]==1 && !visited[i][j]){
                    cnt=0;
                    visited[i][j]=true;
                    dfs(j,i);
                    results.add(cnt);
                }
            }
        }
        Collections.sort(results);
        System.out.println(results.size());
        for (Integer result : results) {
            System.out.println(result);
        }
    }

    public static void dfs(int x, int y){
        cnt+=1;
        for(int k=0;k<4;k++){
            int nx = x + dx[k];
            int ny = y + dy[k];
            if(0<=nx && nx<N && 0<=ny && ny<N){
                if (graph[ny][nx]==1 && !visited[ny][nx]){
                    visited[ny][nx]=true;
                    dfs(nx,ny);
                }
            }
        }
    }
}