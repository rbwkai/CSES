# Next Prime

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Given a positive integer $n$, find the next prime number after it.


## Input


The first line has an integer $t$: the number of tests.


After that, each line has a positive integer $n$.


## Output


For each test, print the next prime after $n$.


## Constraints


- $1 \le t \le 20$
- $1 \le n \le 10^{12}$


## Example


Input:


```
5
1
2
3
42
1337
```


Output:


```
2
3
5
43
1361
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
using ll = __uint64_t; //long long;
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
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;


ll mulmod(ll a, ll b, ll m){
  ll res = 0;
  a%=m;
  while(b){
    if(b&1) res = (res+a)%m;
    a = (a+a)%m;
    b>>=1;
  }
  return res;
}

ll powmod(ll a,ll b,ll m){
  ll res=1;
  a%=m;
  while(b){
    if(b&1) res=mulmod(res, a, m);
    a=mulmod(a, a, m);
    b>>=1;
  }
  return res;
}

//Miller-Rabin
bool is_prime(ll n){
  if(n<2) return false;
  if(n==2 or n==3) return true;
  if(n%2==0) return false;

  ll d=n-1, s=0;
  while((d&1)==0) d>>=1, ++s;

  vi bases = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
  for(ll a: bases){
    if(a>=n) break;
    ll x = powmod(a, d, n);
    if(x==1 or x==n-1) continue;

    bool ok = false;
    for (ll r=1; r<s; ++r) {
      x = mulmod(x, x, n);
      if (x == n-1){ok = true; break;}
    }
    if (!ok) return false;
  }
  return true;
}

void solve(){
  ll n; cin>>n;
  if (n==1) {cout<<2<<en; return;}

  n += (n%2==0? 1: 2);
  while (!is_prime(n)) n += 2;
  cout<<n<<en;
}


int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
