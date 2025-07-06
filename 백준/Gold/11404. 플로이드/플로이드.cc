#include <iostream>
#include <vector>
#include <algorithm>
#define INF 1000000000

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m;
    int start, end, weight;
    cin >> n >> m;
    vector<vector<int>> v(102, vector<int> (102,INF));
    for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (i == j) v[i][j] = 0;
		}
	}
    for(int i=0; i<m; i++){
        cin >> start >> end >> weight;
        v[start][end] = min(v[start][end],weight);
    }
    for(int k=1; k<=n; k++){
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                v[i][j] = min(v[i][j], v[i][k] + v[k][j]);
            }
        }
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(v[i][j] == INF) v[i][j] = 0;
            cout << v[i][j] << ' ';
        } 
        cout << "\n";
    }
    return 0;
}