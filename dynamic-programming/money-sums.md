# Money Sums

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You have $n$ coins with certain values. Your task is to find all money sums you can create using these coins.


## Input


The first input line has an integer $n$: the number of coins.


The next line has $n$ integers $x_1,x_2,\dots,x_n$: the values of the coins.


## Output


First print an integer $k$: the number of distinct money sums. After this, print all possible sums in increasing order.


## Constraints


- $1 \le n \le 100$
- $1 \le x_i \le 1000$


## Example


Input:


```
4
4 2 5 2
```


Output:


```
9
2 4 5 6 7 8 9 11 13
```


---

## Solution

```cpp
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using vi = vector<ll>;
using pii = pair<ll, ll>;
using grid = vector<vi>;

#define fix(_oO) cout<<setprecision(_oO)<<fixed
#define fir(_oO) for(int i=0; i<_oO; ++i)
#define fjr(_oO) for(int j=0; j<_oO; ++j)
const ll mod = 1e9+7;

void solve(){
  ll n; cin>>n;
  set<int> st={0};

  while(n--){
    int c; cin>>c;
    set<int> tm; 
    for(int t: st) tm.insert(t);
    for(int t: st) tm.insert(t+c);
    swap(tm, st);
  }
  cout<<st.size()-1<<endl;
  for(int s: st) if(s) cout<<s<<" ";
  cout<<endl;
}


int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int tC=1; //cin>>tC;
  while(tC--){
    solve();
  }
}
```
