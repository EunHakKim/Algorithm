import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static long A, B;
    public static StringTokenizer st;
    public static StringBuilder sb;
    public static Queue<Long> queue;
    public static long cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st= new StringTokenizer(br.readLine());
        sb= new StringBuilder();
        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());

        bfs(A, B);
        System.out.println(-1);
    }

    public static void bfs(long a, long b){
        queue = new LinkedList<>();
        queue.offer(a);
        cnt=0;

        while (!queue.isEmpty()){
            int size = queue.size();
            for(int i=0;i<size;i++) {
                long temp = queue.poll();
                if (temp == b) {
                    System.out.println(cnt + 1);
                    System.exit(0);
                }
                if (temp * 2 <= b) {
                    queue.offer(temp * 2);
                }
                if (temp * 10 + 1 <= b) {
                    queue.offer(temp * 10 + 1);
                }
            }
            cnt++;
        }
    }
}