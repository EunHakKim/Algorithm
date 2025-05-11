import java.io.*;
import java.util.*;

public class Main {
    public static int n, k, idx;
    public static List<Integer> arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken()) - 1;
        idx = k;
        arr = new ArrayList<>();

        for (int i = 1; i < n + 1; i++) {
            arr.add(i);
        }

        System.out.print("<");
        while (arr.size() > 1) {
            int temp = arr.remove(idx);
            System.out.print(temp);
            System.out.print(", ");
            idx = (idx + k) % arr.size();
        }
        System.out.print(arr.get(0));
        System.out.print(">");
    }
}