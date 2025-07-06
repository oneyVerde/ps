#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, size; cin >> n >> size;
    vector<int> v(n);
    for(int i=0; i<n; i++) cin >> v[i];
    sort(v.begin(), v.end());
    for(int i=0; i<n; i++){
        if(v[i] <= size) size++;
    }
    cout << size;
    
    return 0;
}