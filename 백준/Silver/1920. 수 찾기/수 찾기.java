import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    List<Integer> A = new ArrayList<>();
    int ANS;
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            A.add(Integer.parseInt(st.nextToken()));
        }

        A.sort(Comparator.naturalOrder());

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<m; i++) {
            int t = Integer.parseInt(st.nextToken());
            ANS = 0;
            binarySearch(t, 0, n-1);
            bw.write(ANS+"\n");
            bw.flush();
        }
        br.close();
        bw.close();
    }

    public void binarySearch(int target, int start, int end) {
        if (start > end) return;
        int mid = (start + end) / 2;
        if (A.get(mid) == target) {
            ANS = 1;
        } else if (A.get(mid) < target){
            binarySearch(target, mid+1, end);
        } else {
            binarySearch(target, start, mid-1);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}