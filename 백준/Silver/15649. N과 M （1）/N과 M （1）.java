
import java.io.*;
import java.util.*;

public class Main {
    public static int n, m;
    public static List<Integer> list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        list = new ArrayList<>();

        back(n, m, list);
    }

    public static void back(int n, int m, List<Integer> list) {
        if (list.size() == m) {
            for(Integer x : list) {
                System.out.print(x + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i < n + 1; i++) {
            if (!list.contains(i)) {
                list.add(i);
                back(n, m, list);
                list.remove(list.size() - 1);
            }
        }
    }
}