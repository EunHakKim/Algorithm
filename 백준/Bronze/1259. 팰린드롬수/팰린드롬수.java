import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String s = br.readLine();
            if (s.equals("0")) {
                break;
            }
            boolean isP = true;
            int len = s.length();

            for (int i = 0; i < len / 2; i++) {
                if (s.charAt(i) != s.charAt(len - i - 1)) {
                    isP = false;
                    break;
                }
            }

            if (isP) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
    }
}