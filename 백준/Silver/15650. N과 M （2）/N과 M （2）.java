import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    int N, M;
    List<Integer> arr;
    boolean[] VISIT;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;

    public void solution() throws Exception {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        VISIT = new boolean[N+1];
        arr = new ArrayList<>();

        backtrack(1, 0);
        br.close();
        bw.close();
    }

    public void backtrack(int start, int depth) throws Exception {
        if (depth == M) {
            for (int i=0; i<M; i++) {
                bw.write(arr.get(i) +" ");
            }
            bw.write("\n");
            bw.flush();
            return;
        }

        for (int i=start; i<=N; i++) {
            if (VISIT[i]) continue;
            VISIT[i] = true;
            arr.add(i);
            backtrack(i+1, depth+1);
            VISIT[i] = false;
            arr.remove(arr.size()-1);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}