import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] arr, oper = new int[4];
    static int MIN = Integer.MAX_VALUE;
    static int MAX = Integer.MIN_VALUE;

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;

    public void solution() throws Exception {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<4; i++) {
            oper[i] = Integer.parseInt(st.nextToken());
        }

        backtrack(arr[0], 0);
        bw.write(MAX+"\n");
        bw.write(MIN+"");

        bw.flush();
        br.close();
        bw.close();
    }

    public void backtrack(int sum, int depth) {
        if (depth == N-1) {
            if (sum > MAX) MAX = sum;
            if (sum < MIN) MIN = sum;

            return;
        }

        for (int i=0; i<4; i++) {
            if (oper[i] <= 0) continue;
            oper[i]--;
            sum = operate(sum, i, arr[depth+1]);
            backtrack(sum, depth+1);
            oper[i]++;
            sum = reverseOperate(sum, i, arr[depth+1]);
        }
    }

    public int operate(int sum, int operation, int val) {
        if (operation == 0) sum += val;
        if (operation == 1) sum -= val;
        if (operation == 2) sum *= val;
        if (operation == 3) sum /= val;
        return sum;
    }

    public int reverseOperate(int sum, int operation, int val) {
        if (operation == 0) sum -= val;
        if (operation == 1) sum += val;
        if (operation == 2) sum /= val;
        if (operation == 3) sum *= val;
        return sum;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}