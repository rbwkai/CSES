# Ferris Wheel

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ children who want to go to a Ferris wheel, and your task is to find a gondola for each child.


Each gondola may have one or two children in it, and in addition, the total weight in a gondola may not exceed $x$. You know the weight of every child.


What is the minimum number of gondolas needed for the children?


## Input


The first input line contains two integers $n$ and $x$: the number of children and the maximum allowed weight.


The next line contains $n$ integers $p_1,p_2,\ldots,p_n$: the weight of each child.


## Output


Print one integer: the minimum number of gondolas.


## Constraints


- $1 \le n \le 2 \cdot 10^5$
- $1 \le x \le 10^9$
- $1 \le p_i \le x$


## Example


Input:


```
4 10
7 2 3 9
```


Output:


```
3
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

ll mod=1e9+7;

void solve(){
  ll n, x; cin>>n>>x;
  vi v(n); fir(n) cin>>v[i];
  sort(v.begin(), v.end());

  ll l=0, r=n-1, cnt=0;
  while(l<r){
    if(v[l]+v[r]<=x) l++;
    r--; cnt++;
  }
  cout<<cnt+(l==r)<<endl;
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int tC=1; // cin>>tC;
  while(tC--){
    solve();
  }
}
```
