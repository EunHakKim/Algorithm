import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static int N;
    public static int M;
    public static int[][] graph;
    public static boolean[] visited;
    public static Queue<Integer> queue;
    public static int result;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N=sc.nextInt();
        M=sc.nextInt();

        graph = new int[101][101];
        visited = new boolean[101];

        for(int i=1;i<M+1;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            graph[a][b]=1;
            graph[b][a]=1;
        }

        bfs(1);
    }

    public static void bfs(int index){
        queue = new LinkedList<>();

        visited[index]=true;
        queue.offer(index);
        result=0;
        while (!queue.isEmpty()){
            int temp = queue.poll();
            result+=1;
            for(int i=1;i<N+1;i++){
                if(graph[temp][i]==1 && !visited[i]){
                    queue.offer(i);
                    visited[i]=true;
                }
            }
        }
        System.out.println(result-1);
    }
}