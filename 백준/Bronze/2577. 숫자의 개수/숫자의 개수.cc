#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int inputArr[3];
    for(int i=0; i<3; i++) cin >> inputArr[i];
    
    long long answer = 0;
    answer = inputArr[0] * inputArr[1] * inputArr[2];
    string sAns = to_string(answer);
    
    int freq[10];
    fill(freq, freq+10, 0);

    for(char c : sAns) {
        int b = c-'0';
        freq[b]++;
    }
    for(int i=0; i<10; i++) cout << freq[i] << '\n';
}