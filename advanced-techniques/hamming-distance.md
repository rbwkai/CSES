# Hamming Distance

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

The Hamming distance between two strings $a$ and $b$ of equal length is the number of positions where the strings differ.


You are given $n$ bit strings, each of length $k$ and your task is to calculate the minimum Hamming distance between two strings.


## Input


The first input line has two integers $n$ and $k$: the number of bit strings and their length.


Then there are $n$ lines each consisting of one bit string of length $k$.


## Output


Print the minimum Hamming distance between two strings.


## Constraints


- $2 \le n \le 2 \cdot 10^4$
- $1 \le k \le 30$


## Example


Input:


```
5 6
110111
001000
100001
101000
101110
```


Output:


```
1
```


Explanation: The strings 101000 and 001000 differ only at the first position.



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
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  ll n, k, t; cin>>n>>k;
  vi v(n); string s;
  fir(n){
    cin>>s; t=0;
    fjr(k) t|=((s[j]-'0')<<j);
    v[i]=t;
  }
  
  ll res=k+1;
  fir(n) fjr(i) res=min(res, (ll)__builtin_popcount(v[i]^v[j]));
  cout<<res<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
