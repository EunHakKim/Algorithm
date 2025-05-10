
import java.util.*;
import java.io.*;

public class Main {
    public static int n, m, ans;
    public static List[] graph;
    public static boolean[] visited;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        graph = new List[n + 1];
        visited = new boolean[n + 1];

        for(int i = 0;i<n+1;i++) {
            graph[i] = new ArrayList<>();
        }

        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        visited[1] = true;
        ans = 0;
        while (!queue.isEmpty()) {
            int nc = queue.poll();
            for(int i = 0; i < graph[nc].size(); i++) {
                if (!visited[(int)graph[nc].get(i)]) {
                    visited[(int)graph[nc].get(i)] = true;
                    queue.add((int)graph[nc].get(i));
                    ans ++;
                }
            }
        }
        System.out.println(ans);
    }
}
