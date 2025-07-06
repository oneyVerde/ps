#include <iostream>

using namespace std;

long long rec(int n){
    if(n==1) return 1;
    return n*rec(n-1);
}
int main(){
    int n; cin >> n;
    if(n==0){
        cout << 1;
        return 0;
    }
    long long result = rec(n);
    cout << result;
    return 0;
}