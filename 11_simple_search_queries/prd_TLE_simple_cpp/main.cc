#include <bits/stdc++.h>
using namespace std;

string S;
int Q;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cin >> S;
  cin >> Q;
  for(int i=0; i<Q; i++) {
    string t;
    cin >> t;
    if (S.find(t) == string::npos) {
      cout << "NO" << endl;
    } else {
      cout << "YES" << endl;
    }
  }
  return 0;
}
