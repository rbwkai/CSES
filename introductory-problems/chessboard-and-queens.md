# Chessboard and Queens

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Your task is to place eight queens on a chessboard so that no two queens are attacking each other. As an additional challenge, each square is either free or reserved, and you can only place queens on the free squares. However, the reserved squares do not prevent queens from attacking each other.


How many possible ways are there to place the queens?


## Input


The input has eight lines, and each of them has eight characters. Each square is either free (.) or reserved (*).


## Output


Print one integer: the number of ways you can place the queens.


## Example


Input:


```
........
........
..*.....
........
........
.....**.
...*....
........
```


Output:


```
65
```


---

## Solution

```cpp
//#pragma GCC optimize("Ofast,unroll-loops")
//#pragma GCC target("avx2,popcnt,lzcnt,abm,bmi,bmi2,fma,tune=native")

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
using ll = long long;
using vi = vector<ll>;
using pi = pair<ll, ll>;
using grid = vector<vi>;

template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = LLONG_MAX-3e5; //0x3f3f3f3f3f3f;
ll const mod = 998244353; //1e9+7;


void solve(){
  vector<string> v(8);
  fir(8) cin>>v[i];

  ll res=0;
  set<ll> col, psd, ngd;
  function<void(ll)> rec=[&](ll r){
    if(r==8){
      res++;
      return;
    }
    fir(8) if(v[r][i]=='.'){
      if(col.find(i)==col.end() and
         psd.find(i+r)==psd.end() and
         ngd.find(i-r)==ngd.end()){
        col.insert(i); psd.insert(i+r); ngd.insert(i-r);
        rec(r+1);
        col.erase(i); psd.erase(i+r); ngd.erase(i-r);
      }
    }
  };
  rec(0);
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}
```
