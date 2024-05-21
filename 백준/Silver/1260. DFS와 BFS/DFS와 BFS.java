import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static int[][] graph;
    public static boolean[] visited;
    public static Queue<Integer> queue;
    public static int N;
    public static int M;
    public static int V;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        V = sc.nextInt();

        graph = new int[1001][1001];
        visited = new boolean[1001];

        for(int i=0; i<M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a][b]=1;
            graph[b][a]=1;
        }

        dfs(V);
        System.out.println();

        Arrays.fill(visited, false);
        bfs(V);

    }

    public static void bfs(int index) {
        queue = new LinkedList<>();

        visited[index]=true;
        queue.offer(index);
        System.out.print(index + " ");

        while(!queue.isEmpty()) {
            int temp = queue.poll();

            for(int i=1;i<N+1;i++) {
                if (graph[temp][i]==1 && !visited[i]){
                    queue.offer(i);
                    visited[i]=true;
                    System.out.print(i + " ");
                }
            }
        }
        System.out.println();
    }

    public static void dfs(int index) {
        visited[index]=true;
        System.out.print(index + " ");

        for(int i=1;i<N+1;i++){
            if(graph[index][i]==1 && !visited[i]){
                visited[i]=true;
                dfs(i);
            }
        }
    }
}