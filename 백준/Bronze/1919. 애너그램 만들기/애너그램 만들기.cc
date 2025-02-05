#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int a[26] = {};
    string str1, str2;
    cin>>str1;
    for(auto c : str1) a[c-'a']++;
    cin>>str2;
    for(auto c : str2) a[c-'a']--;
    int ans = 0;
    for(auto i : a) {
        if(abs(i)) ans+=abs(i);
    }
    cout<<ans;
}