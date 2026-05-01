# Apartments

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

There are $n$ applicants and $m$ free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.


Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.


## Input


The first input line has three integers $n$, $m$, and $k$: the number of applicants, the number of apartments, and the maximum allowed difference.


The next line contains $n$ integers $a_1, a_2, \ldots, a_n$: the desired apartment size of each applicant. If the desired size of an applicant is $x$, they will accept any apartment whose size is between $x-k$ and $x+k$.


The last line contains $m$ integers $b_1, b_2, \ldots, b_m$: the size of each apartment.


## Output


Print one integer: the number of applicants who will get an apartment.


## Constraints


- $1 \le n, m \le 2 \cdot 10^5$
- $0 \le k \le 10^9$
- $1 \le a_i, b_i \le 10^9$


## Example


Input:


```
4 3 5
60 45 80 60
30 60 75
```


Output:


```
2
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
  ll n, m, k; cin>>n>>m>>k;
  vi nn(n); fir(n) cin>>nn[i];
  vi mm(m); fir(m) cin>>mm[i];

  sort(nn.begin(), nn.end());
  sort(mm.begin(), mm.end());

  ll np=0, mp=0, cnt=0;
  
  while(n-np and m-mp){
    if(abs(nn[np]-mm[mp])<=k){
      np++; mp++; cnt++;
    }
    else if(nn[np]-mm[mp]>k){
      mp++;
    }
    else np++;
  }
  cout<<cnt<<endl;
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
