#include <iostream>

using namespace std;

int main(){
    int tmp, max = 0, row, col;

    for(int i=1; i<=9; i++)
        for(int j=1; j<=9; j++){
            cin >> tmp;
            if(tmp >= max){
                max = tmp;
                row = i; col = j;
            }
        }
    cout << max << "\n" << row << ' ' << col;
    return 0;
}