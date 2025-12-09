import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++){
            Stack<String> stack = new Stack<>();
            String str = br.readLine();
            for (String c: str.split("")) {
                if(c.equals("(")){
                    stack.push(c);
                } else {
                    if (!stack.empty()) {
                        stack.pop();
                    } else { // ) 부터 입력되면 NO이므로
                        stack.push(")");
                        break;
                    }
                }
            }
            if (stack.empty()) bw.write("YES");
            else bw.write("NO");
            bw.write("\n");
            bw.flush();
        }
        br.close();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}