# Digit Queries

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

Consider an infinite string that consists of all positive integers in increasing order:


12345678910111213141516171819202122232425...


Your task is to process $q$ queries of the form: what is the digit at position $k$ in the string?


## Input


The first input line has an integer $q$: the number of queries.


After this, there are $q$ lines that describe the queries. Each line has an integer $k$: a $1$-indexed position in the string.


## Output


For each query, print the corresponding digit.


## Constraints


- $1 \le q \le 1000$
- $1 \le k \le 10^{18}$


## Example


Input:


```
3
7
19
12
```


Output:


```
7
4
1
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

vi cp(20, 9);
ordered_set<ll> os;
void pre(){
  ll N=17;
  fir(N) cp[i]*=(i+1);
  fir(N) fjr(i) cp[i]*=10;

  ll ps=0; os.insert(0);
  fir(N) ps+=cp[i], os.insert(ps);
}

void solve(){
  ll n; cin>>n;
  ll lft=*os.lower_bound(n);
  ll nd=os.order_of_key(lft)-1;
  ll ld=*os.find_by_order(nd);
  ll wd=n-ld;
  ll dv=(wd+nd)/(nd+1), md=wd%(nd+1);
  ll ac=cp[nd]/(9*(nd+1))+dv-1;

  ll dr=nd+1-(!md? nd+1: md);
  while(dr--) ac/=10;
  cout<<ac%10<<en;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  pre();

  int tt = 1; cin>>tt;
  fir(tt){
    //cout<<"Case "<<i+1<<": ";
    solve();
  }
}
```
