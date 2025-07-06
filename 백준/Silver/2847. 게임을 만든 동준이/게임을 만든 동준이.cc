#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, cnt=0; cin >> n;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin >> v[i];
    }
    for(int i=n-1; i>0; i--){
        while(v[i] <= v[i-1]){
            v[i-1]--;
            cnt++;
        }
    }
    cout << cnt;
    
    return 0;
}