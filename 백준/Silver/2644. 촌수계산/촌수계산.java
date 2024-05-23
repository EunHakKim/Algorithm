import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static int n, m, a, b;
    public static StringTokenizer st;
    public static int[][] graph;
    public static boolean[] visited;
    public static int[] result;
    public static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        a=Integer.parseInt(st.nextToken());
        b=Integer.parseInt(st.nextToken());
        m = Integer.parseInt(br.readLine());

        graph = new int[101][101];
        visited = new boolean[101];
        result = new int[101];
        for(int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x][y]=1;
            graph[y][x]=1;
        }

        result[a]=0;
        visited[a]=true;
        bfs(a);
        System.out.println(-1);
    }

    public static void bfs(int index){
        queue = new LinkedList<>();
        queue.offer(index);

        while(!queue.isEmpty()){
            int temp = queue.poll();
            for(int i=1;i<n+1;i++){
                if(graph[temp][i]==1 && !visited[i]){
                    visited[i]=true;
                    result[i]=result[temp]+1;
                    if(i==b){
                        System.out.println(result[b]);
                        System.exit(0);
                    }
                    queue.offer(i);
                }
            }
        }
    }
}