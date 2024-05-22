import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static int N;
    public static StringTokenizer st;
    public static ArrayList<Integer> graph[];
    public static boolean[] visited;
    public static int[] parent;
    public static Queue<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());

        graph = new ArrayList[N+1];
        for(int i=0;i<N+1;i++)
            graph[i]=new ArrayList<>();
        visited = new boolean[N+1];
        parent = new int[N+1];
        for(int i=0;i<N-1;i++){
            st = new StringTokenizer(br.readLine());
            int a= Integer.parseInt(st.nextToken());
            int b= Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        bfs(1);
        for(int i=2;i<N+1;i++){
            System.out.println(parent[i]);
        }
    }

    public static void bfs(int index){
        queue = new LinkedList<>();
        visited[index]=true;
        queue.offer(index);

        while (!queue.isEmpty()){
            int temp = queue.poll();
            for(int i:graph[temp]){
                if(!visited[i]){
                    visited[i]=true;
                    queue.offer(i);
                    parent[i]=temp;
                }
            }
        }
    }
}