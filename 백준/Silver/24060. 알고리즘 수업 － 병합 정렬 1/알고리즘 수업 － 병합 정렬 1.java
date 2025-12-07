import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    int SIZE, COUNT=0, K, ANS = -1;
    int[] TMP;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        SIZE = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        int[] arr = new int[SIZE];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<SIZE; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        TMP = new int[SIZE+1];
        merge_sort(arr,0, SIZE-1);
        bw.write(ANS+"");
        bw.flush();
        br.close();
        bw.close();
    }

    public void merge_sort(int[] A, int p, int r) {
        if (p < r) {
            int q = (p+r) / 2;
            merge_sort(A, p, q);
            merge_sort(A, q+1, r);
            merge(A, p, q, r);
        }
    }

    public void merge(int[] A, int p, int q, int r) {
        int i = p, j = q+1, t = p;
        while (i <= q && j <= r) {
            if (A[i] <= A[j]) TMP[t++] = A[i++];
            else TMP[t++] = A[j++];
        }
        while (i <= q) {
            TMP[t++] = A[i++];
        }
        while (j <= r) {
            TMP[t++] = A[j++];
        }
        i = p; t = p;
        while(i <= r) {
            A[i] = TMP[t];
            COUNT++;
            if (COUNT == K) ANS = A[i];
            i++; t++;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}