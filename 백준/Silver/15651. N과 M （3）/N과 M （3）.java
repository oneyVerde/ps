import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    int N, M;
    List<Integer> arr;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;

    public void solution() throws Exception {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new ArrayList<>();

        backtrack(0);
        bw.flush();
        br.close();
        bw.close();
    }

    public void backtrack(int depth) throws Exception {
        if (depth == M) {
            for(int num: arr) bw.write(num+" ");
            bw.write("\n");
            return;
        }

        for (int i=1; i<=N; i++) {
            arr.add(i);
            backtrack(depth+1);
            arr.remove(arr.size()-1);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}