#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(){
    int n; cin >> n;
    stack<int> st;
    vector<int> v(n+1), f(1000001), ngf(1000001, -1);
    
    for(int i=1; i<=n; i++){
        cin >> v[i];
        f[v[i]]++;
    }
    for(int i=n; i>0; i--){
        while(!st.empty() && f[st.top()] <= f[v[i]])
            st.pop();
        if(!st.empty() && f[st.top()] > f[v[i]])
            ngf[i] = st.top();
        st.push(v[i]);
    }
    for(int i=1; i<=n; i++)
        cout << ngf[i] << ' ';
    return 0;
}