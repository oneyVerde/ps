import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<String> stack = new Stack<>();
        String str = br.readLine();
        boolean tag = false;
        int idx=0, size=str.length()-1;
        for(String s: str.split("")) {

            // tag 확인
            if (s.equals("<")){
                tag = true;
            } else if (s.equals(">")){
                tag = false;
                bw.write(s+"");
            }
            
            if (tag) {
                // < 이전 단어 출력
                if (s.equals("<")){
                    while(!stack.empty()){
                        bw.write(stack.pop()+"");
                    }
                    bw.write(s+"");
                } else {
                    // tag 사이 문자 출력
                    bw.write(s+"");
                }

            }
            // tag가 아니면
            if (!tag) {
                // 공백 기준으로 단어 출력
                if (s.equals(" ")) {
                    while(!stack.empty()){
                        bw.write(stack.pop()+"");
                    }
                    bw.write(" ");
                } else if (!s.equals(">")) {
                    // 끝에 오는 문자라면 이전 단어 출력
                    if (idx == size) {
                        stack.push(s);
                        while(!stack.empty()){
                            bw.write(stack.pop()+"");
                        }
                    } else stack.push(s);
                }
            }
            idx++;
        }
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}