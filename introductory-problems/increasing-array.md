# Increasing Array

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are given an array of $n$ integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.


On each move, you may increase the value of any element by one. What is the minimum number of moves required?


## Input


The first input line contains an integer $n$: the size of the array.


Then, the second line contains $n$ integers $x_1,x_2,\ldots,x_n$: the contents of the array.


## Output


Print the minimum number of moves.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x_i \le 10^9$


## Example


Input:


```
5
3 2 5 1 7
```


Output:


```
5
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

void solve(){
  ll n; cin>>n;
  ll pv, res=0; cin>>pv;
  fir(n-1){
    ll t; cin>>t;
    if(t<pv) res+=pv-t;
    else pv=t;
  }
  cout<<res<<endl;
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
