import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static List<Integer> arr, num;
    static boolean[] VISIT;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;

    public void solution() throws Exception {

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        VISIT = new boolean[N+1];
        arr = new ArrayList<>();
        num = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            num.add(Integer.parseInt(st.nextToken()));
        }
        num.sort(Comparator.naturalOrder());

        backtrack(0, 0);
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

        for (int i=start; i<N; i++) {
            if (VISIT[i]) continue;
            VISIT[i] = true;
            arr.add(num.get(i));
            backtrack(i+1, depth+1);
            VISIT[i] = false;
            arr.remove(arr.size()-1);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}