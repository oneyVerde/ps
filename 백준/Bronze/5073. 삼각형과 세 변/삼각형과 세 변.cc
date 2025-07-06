#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int val;
    
    while(1){
        vector<int>v;
        for(int i=0;i<3;i++){
            cin >> val;
            v.push_back(val);
        }
        if(!v[0]&&!v[1]&&!v[2]) break;
        sort(v.begin(), v.end());
        if(v[0]+v[1]<=v[2])
            cout << "Invalid" << "\n";
        else{
            if(v[0]==v[1]&&v[2]==v[1])
                cout << "Equilateral" << "\n";
            else if(v[0]!=v[1]&&v[0]!=v[2]&&v[1]!=v[2])
                cout << "Scalene" << "\n";
            else cout << "Isosceles" << "\n";
        }
    
    }
    return 0;
}