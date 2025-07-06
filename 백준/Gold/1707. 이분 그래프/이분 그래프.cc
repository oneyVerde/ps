#include <bits/stdc++.h>

using namespace std;

vector<int> graph[20001];
int color[20001];
int v,e,k;
int ans;;

void dfs(int idx, int flag){
    color[idx] = flag;
    for(int i=0; i<graph[idx].size(); i++){
        int next = graph[idx][i];
        if(color[next] == flag){
            ans = 0;
            return;
        }
        else if(ans && color[next] == 0){
            dfs(next, -flag);
        }
    }
}

int main() {
	cin >> k;
    while(k--){
        cin >> v >> e;
        memset(graph, 0, sizeof(graph));
        memset(color, 0, sizeof(color));
        ans = 1;
        for(int i=0; i<e; i++){
            int a,b; cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        for(int i=1; i<=v; i++){
            if(ans && color[i] == 0)
                dfs(i, 1);
        }
        if(ans) cout << "YES\n";
        else cout << "NO\n";
    }
}