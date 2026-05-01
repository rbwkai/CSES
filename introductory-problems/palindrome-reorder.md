# Palindrome Reorder

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).


## Input


The only input line has a string of length $n$ consisting of characters A–Z.


## Output


Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".


## Constraints


- $1 \le n \le 10^6$


## Example


Input:


```
AAAACACBA
```


Output:


```
AACABACAA
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
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=_O-1; i<_O; ++i, --ii)
#define fjr(_O) for(int j=0, jj=_O-1; j<_O; ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


void solve(){
  string s; cin>>s;
  vi v(26); fir(sz(s)) v[s[i]-'A']++;
  ll oc=0, c=0; fir(26) if(v[i]&1) oc++, c=i;
  
  if(oc>1){
    cout<<"NO SOLUTION"<<en;
    return;
  }
  string r="";
  fir(26) r+=string(v[i]/2, 'A'+i);
  string rr=r; reverse(rr.begin(), rr.end());
  if(oc) r+='A'+c;
  cout<<r+rr<<en;
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
