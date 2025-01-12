#include <bits/stdc++.h>
using namespace std;
int a, b, c;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> a >> b >> c;
    if(b<a && c<a) {
        if(c<b) cout << c << ' ' << b << ' ' << a << '\n';
        else if(b<c) cout << b << ' ' << c << ' ' << a << '\n';
    } else if(a<b && c<b) {
        if(c<a) cout << c << ' ' << a << ' ' << b << '\n';
        else if(a<c) cout << a << ' ' << c << ' ' << b << '\n';
    } else if(a<c && b<c) {
        if(b<a) cout << b << ' ' << a << ' ' << c << '\n';
        else cout << a << ' ' << b << ' ' << c << '\n';
    }
    return 0;
}