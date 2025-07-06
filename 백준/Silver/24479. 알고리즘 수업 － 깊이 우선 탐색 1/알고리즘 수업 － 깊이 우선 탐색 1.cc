#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;
vector<int> visited;
int n, cnt = 1;

void dfs(int idx){
    visited[idx] = cnt;
    cnt++;
    for(int i=0; i<graph[idx].size(); i++){
        if(visited[graph[idx][i]] == 0)
            dfs(graph[idx][i]);
    }
}
int main(){
    int m, start; cin >> n >> m >> start;
    int a,b;

    graph.assign(n+1, vector<int>(0,0));
    visited.assign(n+1, 0);

    for(int i=0; i<m; i++){
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for(int i=1; i<=n; i++)
        sort(graph[i].begin(), graph[i].end());

    dfs(start);
    for(int i=1; i<=n; i++){
        cout << visited[i] << "\n";
    }

    return 0;
}