import java.io.*;

public class Main {
    public static int t;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < t; i++) {
            String s = br.readLine();
            int zero = 0;
            int ans = 0;
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == 'O') {
                    zero ++;
                    ans += zero;
                } else {
                    zero = 0;
                }
            }
            System.out.println(ans);
        }
    }
}