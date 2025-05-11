import java.io.*;
import java.util.*;

public class Main {
    public static int n;
    public static Map<String, Integer> books;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        books = new HashMap<>();
        int m = 0;

        for (int i = 0; i < n; i++) {
            String key = br.readLine();
            books.put(key, books.getOrDefault(key, 0) + 1);
            m = Math.max(m, books.get(key));
        }

        List<String> list = new ArrayList<>();
        for(String key : books.keySet()) {
            if (books.get(key) == m) {
                list.add(key);
            }
        }
        Collections.sort(list);
        System.out.println(list.get(0));
    }
}