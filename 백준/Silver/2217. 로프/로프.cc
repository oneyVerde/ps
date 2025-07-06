#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, max=0; cin >> n;
    vector<int> v(n);
    for(int i=0; i<n; i++){
        cin >> v[i];
    }
    sort(v.begin(), v.end(), greater<int>());
    for(int i=0; i<n; i++){
        int w = v[i] * (i+1);
        if(w > max) max = w;
    }
    cout << max;
    
    return 0;
}