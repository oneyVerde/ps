#include <bits/stdc++.h>

using namespace std;

int main(){
    int val, res=0;
    vector<int>v;
    for(int i=0; i<5; i++){
        cin >> val;
        v.push_back(val);
    }
    sort(v.begin(), v.end());
    for(int i=0; i<5; i++){
        res += v[i];
    }
    cout << (int)res/5 << "\n";
    cout << v[2];

    return 0;
}