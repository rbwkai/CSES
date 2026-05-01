# Permuted Binary Strings

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There is a hidden permutation $a_1, a_2,\dots, a_n$ of integers $1, 2,\dots, n$. Your task is to find this permutation.


To do this, you can ask questions: you can choose a binary string $b_1b_2\dots b_n$ and you will receive the binary string $b_{a_1}b_{a_2}\dots b_{a_n}$.


## Interaction


This is an interactive problem. Your code will interact with the grader using standard input and output. You should start by reading a single integer $n$: the length of the permutation.


On your turn, you can print one of the following:


- "$?\ b_1b_2\dots b_n$", where $b_i\in\{0, 1\}$: The grader will return the binary string $b_{a_1}b_{a_2}\dots b_{a_n}$.
- "$!\ a_1\ a_2 \dots a_n$": report that the hidden permutation is $a_1, a_2,\dots, a_n$. Your program must terminate after this.


Each line should be followed by a line break. You must make sure the output gets flushed after printing each line.


## Constraints


- $1 \le n \le 1000$
- you can ask at most $10$ questions of type $?$


## Example

```
3
? 100
100
? 010
001
? 001
010
! 1 3 2
```


Explanation: The hidden permutation is $[1, 3, 2]$. In the first question $b_1b_2b_3 = 100$ and the grader returns $b_{a_1}b_{a_2}b_{a_3} = b_1b_3b_2 = 100$. In the second question $b_1b_2b_3 = 010$ and the grader returns $b_1b_3b_2 = 001$.



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
using ordered_set = tree<T, null_type, less_equal<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)
 
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

string ask(string s){
  cout<<"? "<<s<<en;
  cout.flush();
  string r; cin>>r;
  return r;
}

void solve(){
  ll n; cin>>n;
  vi v(n);

  fjr(10){
    string qs(n, '0'); fir(n) qs[i] += (i>>j)&1;
    string rs = ask(qs);
    fir(n) v[i] |= ((rs[i]=='1')<<j);
  }
  cout<<"! "; 
  fir(n) cout<<v[i]+1<<ln;
  cout.flush();
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
