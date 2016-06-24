#include "proj_euler.h"

LL sq;
LL * kcacheDec;
LL * cache;
LL * gcache;
LL cache_size;

// sum i from 1 to n of floor(n/i)
// Equivalent to sum of number of divisors function.
LL G_sum(LL n,LL k_div)
{
  if (k_div <=sq&&gcache[k_div]) return gcache[k_div];
  LL s = 0;
  LL m = 1;
  LL k = n;
  LL j;
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
    s = s + (j+1)*k;
    m += j + 1;    
  }
  if (k_div <=sq) gcache[k_div] = s;  
  return s;
}


// Sum of 1 over all (i,j) with i*j <= n and gcd(i,j) = 1
LL dec_sum(LL n,LL k)
{
  if (!n) return 0;
  if (n == 1) return 1;
  if (k<=sq &&kcacheDec[k]) return kcacheDec[k];
  if (n<=cache_size && cache[n]) return cache[n];
  LL s = G_sum(n,k);
  LL dec = 0;
  LL j;
  
  for (j = isqrt(n); j > 1; j--)
  {
    dec = dec + dec_sum((n/j)/j, k*j*j);
  }
  
  LL res = s - dec;
  if (k<=sq) kcacheDec[k] = res;
  if (n<=sq) cache[n] = res;
  return res;  
}

LL solve(LL n)
{
  LL s = 0;
  LL m = 1;
  LL k = n;
  LL j;
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
    s = s + (j+1)*dec_sum(k,m);
    m += j + 1;    
  }
  return s;
  
}

int main()
{
  LL i,j;
  LL n = 1000000000000LL;
  cache_size = 100000000LL;
  sq = isqrt(n);
  kcacheDec = big_arr(sq+1,0);
  cache  = big_arr(cache_size+1,1);
  gcache = big_arr(sq+1,0);
  for (i=2;i<=cache_size;i++)
  {
    if (cache[i] == 1)
    {
      for (j = i; j <= cache_size;j+=i)
      {
      	cache[j] *= 2;
      }
    }
    cache[i] += cache[i-1];
  }
  printf("Computed cache 1.\n");  
  printf("g(%lld) = %lld\n",n,(solve(n)+n)/2);
}


