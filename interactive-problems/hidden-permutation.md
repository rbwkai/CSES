# Hidden Permutation

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a hidden permutation $a_1, a_2,\dots, a_n$ of integers $1, 2,\dots, n$. Your task is to find this permutation.


To do this, you can ask questions: you can choose two indices $i$ and $j$ and you will be told if $a_i < a_j$.


## Interaction


This is an interactive problem. Your code will interact with the grader using standard input and output. You should start by reading a single integer $n$: the length of the permutation.


On your turn, you can print one of the following:


- "$?\ i\ j$", where $1 \le i, j \le n$: ask if $a_i < a_j$. The grader will return YES if $a_i < a_j$ and NO otherwise.
- "$!\ a_1\ a_2 \dots a_n$": report that the hidden permutation is $a_1, a_2,\dots, a_n$. Your program must terminate after this.


Each line should be followed by a line break. You must make sure the output gets flushed after printing each line.


## Constraints


- $1 \le n \le 1000$
- you can ask at most $10^4$ questions of type $?$


## Example

```
3
? 3 2
NO
? 3 1
YES
! 3 1 2
```


Explanation: The hidden permutation is $[3, 1, 2]$. The first question asks if $a_3 < a_2$ which is false, so the answer is NO. The second question asks if $a_3 < a_1$ which is true, so the answer is YES.



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
using pii = pair<ll, ll>;
using grid = vector<vi>;
 
template<class T>
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

struct mint{
  ll v; 
  mint(ll _v=0) {v = (_v%mod +mod)%mod;}

  friend mint operator+(const mint& a, const mint& b){ return mint(a.v + b.v); }
  friend mint operator-(const mint& a, const mint& b){ return mint(a.v - b.v); }
  friend mint operator*(const mint& a, const mint& b){ return mint(a.v * b.v); }
  friend mint operator/(const mint& a, const mint& b){ return a*minv(b); }
  friend mint mpow(const mint& b, ll p){
    mint a=b, r=1;
    for( ; p; p>>=1, a=a*a) if(p&1) r=r*a;
    return r;
  }
  friend mint minv(const mint& a){ return mpow(a, mod-2); }
  friend ostream& operator<<(ostream &os, mint m){ return os<<m.v; }
  friend istream& operator>>(istream &is, mint &m){ ll x; is>>x; m=mint(x); return is; }
}; 

bool ask(ll i, ll j){
  cout<<"? "<<i+1<<" "<<j+1<<endl;
  string s; cin>>s;
  return s=="YES";
}
void ans(vi &v){
  cout<<"! ";
  fir(sz(v)) cout<<v[i]<<" ";
  cout<<endl;
}

void ssort(vi &v){
  ll n = sz(v);
  if(n<2) return;

  ll mp=0;
  fir(n) if(i and ask(v[i], mp)) mp=v[i]; 

  vi sorted; sorted.reserve(n);
  sorted.push_back(mp);

  for(ll x: v){
    if(x==mp) continue;

    ll lo=0, hi=sz(sorted);
    while(lo<hi){
      ll md = (lo+hi)/2;
      if(ask(x, sorted[md])) hi=md;
      else lo=md+1;
    }
    sorted.insert(sorted.begin()+lo, x);
  }
  v = sorted;
}

void solve(){
  ll n; cin>>n;
  vi v(n); fir(n) v[i]=i;

  ssort(v);

  vi res(n); fir(n) res[v[i]]=i+1;
  ans(res);
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
