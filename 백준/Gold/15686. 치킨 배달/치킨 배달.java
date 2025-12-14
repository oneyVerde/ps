import java.io.*;
import java.util.*;

class Coordinate {
    int x;
    int y;
    Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int N, M;
    static int[][] arr;
    static ArrayList<Coordinate> house;
    static ArrayList<Coordinate> chicken;
    static int TOTAL;
    static boolean[] OPEN;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][N];
        house = new ArrayList<>();
        chicken = new ArrayList<>();


        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 1) house.add(new Coordinate(i,j));
                if (arr[i][j] == 2) chicken.add(new Coordinate(i,j));
            }
        }

        OPEN = new boolean[chicken.size()];
        TOTAL = Integer.MAX_VALUE;
        chicken(0,0);
        bw.write(TOTAL+"");
        bw.flush();
        bw.close();
        br.close();
    }

    public void chicken(int start, int cnt) {
        if (cnt == M) minDistance(house.size(), chicken.size());
        for (int i=start; i<chicken.size(); i++) {
            OPEN[i] = true;
            chicken(i+1, cnt+1);
            OPEN[i] = false;
        }
    }

    public void minDistance(int houseNum, int chickenNum) {
        int res = 0;
        for(int i=0; i<houseNum; i++) {
            int min = Integer.MAX_VALUE;
            for (int j=0; j<chickenNum; j++) {
                if (OPEN[j]) {
                    int distance = Math.abs(house.get(i).x - chicken.get(j).x) + Math.abs(house.get(i).y - chicken.get(j).y);
                    min = Math.min(min, distance);
                }
            }
            res += min;
        }
        TOTAL = Math.min(TOTAL, res);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}