#include <bits/stdc++.h>

using namespace std;

int main(){
    while(1){
        string s; getline(cin, s);
        vector<int>v(27);
        if(s[0] == '#') break;
        int n = s.length();
        for(int i = 0; i<n; i++){
            if((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')){
                if(s[i] >= 'a' && s[i] <= 'z')
                    s[i] -= 32;
                s[i] -= 65;
                int a = s[i];
                v[a]++;
            }
        }
        int cnt=0;
        for(int i = 0; i<27; i++){
            if(v[i] != 0) cnt++;
        }
        cout << cnt << "\n";
    }

    return 0;
}