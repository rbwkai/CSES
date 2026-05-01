# Book Shop

**Time limit: 1.00 s**  
**Memory limit: 512 MB**

---

## Problem

You are in a book shop which sells $n$ different books. You know the price and number of pages of each book.


You have decided that the total price of your purchases will be at most $x$. What is the maximum number of pages you can buy? You can buy each book at most once.


## Input


The first input line contains two integers $n$ and $x$: the number of books and the maximum total price.


The next line contains $n$ integers $h_1,h_2,\ldots,h_n$: the price of each book.


The last line contains $n$ integers $s_1,s_2,\ldots,s_n$: the number of pages of each book.


## Output


Print one integer: the maximum number of pages.


## Constraints


- $1 \le n \le 1000$
- $1 \le x \le 10^5$
- $1 \le h_i, s_i \le 1000$


## Example


Input:


```
4 10
4 8 5 3
5 12 8 1
```


Output:


```
13
```


Explanation: You can buy books 1 and 3. Their price is $4+5=9$ and the number of pages is $5+8=13$.



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
const ll mod = 1e9+7;

void solve(){
  ll n, x; cin>>n>>x;
  vi c(n); fir(n) cin>>c[i];
  vi v(n); fir(n) cin>>v[i];

  vi dp(x+1, 0);
  fir(n) for(int j=x; j-c[i]>=0; j--){
    dp[j]=max(dp[j], dp[j-c[i]]+v[i]);
  }
  cout<<dp[x]<<endl;
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
