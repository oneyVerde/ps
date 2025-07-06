#include <bits/stdc++.h>

using namespace std;

int main(){
    int n; cin >> n;
    string s; cin >> s;
    vector<int> v(n);
    int max = 0;
    string adrian = "ABC", bruno = "BABC", goran = "CCAABB";
    for(int i=0; i<3; i++){
        int res = 0;
        for(int j=0; j<n; j++){
            if(i == 0){
                if(s[j] == adrian[j%3]) res++;
            }
            else if(i == 1){
                if(s[j] == bruno[j%4]) res++;
            }
            else{
                if(s[j] == goran[j%6]) res++;
            }
        }
        if(res >= max){
            max = res;
        }
        v[i] = res;
    }
    cout << max << "\n";
    for(int i=0; i<3; i++){
        if(v[i] == max){
            if(i == 0) cout << "Adrian\n";
            else if(i == 1) cout << "Bruno\n";
            else cout << "Goran\n";
        }
    }

    return 0;
}