import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Template {

  public static BufferedReader br;
  public static PrintWriter out;
  public static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    out = new PrintWriter(new OutputStreamWriter(System.out));

    out.close();
  }

  private static String next() throws IOException {
    while (st == null || !st.hasMoreTokens())
      st = new StringTokenizer(br.readLine().trim());
    return st.nextToken();
  }

  private static long readLong() throws IOException {
    return Long.parseLong(next());
  }

  private static int readInt() throws IOException {
    return Integer.parseInt(next());
  }

  private static double readDouble() throws IOException {
    return Double.parseDouble(next());
  }

  private static char readCharacter() throws IOException {
    return next().charAt(0);
  }

  private static String readLine() throws IOException {
    return br.readLine().trim();
  }
}