#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    
    string word;
    cin >> word;

    vector<int> alphabet(26);
    for(char a : word) alphabet[a-97]++;
    for(int b : alphabet) cout<< b << ' ';
}