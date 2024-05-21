import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int N, M;
    public static int[][] graph;
    public static boolean[] visited;
    public static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[1001][1001];
        visited = new boolean[1001];

        for(int i=0;i<M;i++){
            StringTokenizer stringTokenizer = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(stringTokenizer.nextToken());
            int b = Integer.parseInt(stringTokenizer.nextToken());
            graph[a][b]=1;
            graph[b][a]=1;
        }

        cnt=0;
        for(int i=1;i<N+1;i++){
            if(!visited[i]){
                cnt+=1;
                dfs(i);
            }
        }
        System.out.println(cnt);
    }

    public static void dfs(int index){
        for(int i=1;i<N+1;i++){
            if(graph[index][i]==1 && !visited[i]){
                visited[i]=true;
                dfs(i);
            }
        }
    }
}