import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static List<Integer> arr, num;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;

    public void solution() throws Exception {

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new ArrayList<>();
        num = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            num.add(Integer.parseInt(st.nextToken()));
        }
        num.sort(Comparator.naturalOrder());

        backtrack(0);
        bw.flush();
        br.close();
        bw.close();
    }

    public void backtrack(int depth) throws Exception {
        if (depth == M) {
            for (int i=0; i<M; i++) {
                bw.write(arr.get(i) +" ");
            }
            bw.write("\n");
            return;
        }

        for (int i=0; i<N; i++) {
            arr.add(num.get(i));
            backtrack(depth+1);
            arr.remove(arr.size()-1);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}