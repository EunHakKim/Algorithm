import java.util.Scanner;

public class Main {

    public static int T;
    public static int M;
    public static int N;
    public static int K;
    public static int[][] graph;
    public static boolean[][] visited;
    public static int cnt;
    public static int[] dx = {1,0,-1,0};
    public static int[] dy = {0,-1,0,1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        T = sc.nextInt();
        for (int i=0;i<T;i++){
            M = sc.nextInt();
            N = sc.nextInt();
            K = sc.nextInt();

            graph = new int[51][51];
            visited = new boolean[51][51];
            for(int j=0;j<K;j++){
                int a = sc.nextInt();
                int b = sc.nextInt();
                graph[b][a]=1;
            }

            cnt=0;
            for(int j=0;j<N;j++){
                for(int k=0;k<M;k++){
                    if(graph[j][k]==1 && !visited[j][k]){
                        cnt+=1;
                        visited[j][k]=true;
                        dfs(k,j);
                    }
                }
            }
            System.out.println(cnt);
        }
    }

    public static void dfs(int x, int y){
        for (int q=0;q<4;q++){
            int nx = x+dx[q];
            int ny = y+dy[q];

            if(0<=nx && nx<M && 0<=ny && ny<N){
                if(graph[ny][nx]==1 && !visited[ny][nx]){
                    visited[ny][nx]=true;
                    dfs(nx,ny);
                }
            }
        }
    }
}