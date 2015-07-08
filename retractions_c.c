#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//#define CAP 100000000000000LL
#define CAP 10000000LL

typedef long long int LL;
//#include <primes.h>

LL mod;
LL sq;
LL * kcache;
LL * kcacheDec;

//sum of i over all pairs (i,j) with i*j <= n
//Equivalent to sum i=1 to i=n i*floor(n/i)
//However, n/i is constant over large ranges, so I want to take advantage of that.
//The i multiplier is tricky, but I can take care of it by using the formula for the sum of an arithmetic progression.
LL F_sum_slow(LL n)
{
  LL i;
  LL s = 0;
  for (i=1;i<=n;i++)
  {
    s += i*(n/i);
  }
  return s;
}

LL isqrt(LL n)
{
    LL x = n;
    LL y = (x + 1) / 2;
    while (y < x)
    {
        x = y;
        y = (x + n / x) / 2;
    }
    return x;
}

// sum i=1 to i=n i*floor(n/i) modulo mod
LL F_sum(LL n)
{
  LL s = 0;
  LL m = 1;
  LL k = n;
  LL j;
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
    LL j_t = j % mod;
    LL coeff = ((m % mod) * (j_t + 1) % mod + ((j_t)*(j_t+1) / 2) % mod) % mod;
    s = (s + coeff*k) % mod;
    
    m += j + 1;    
  }
  return s;
}


// Sum of i over all (i,j) with i*j <= n and gcd(i,j) = 1
LL retraction_sum(LL n,LL k)
{
  if (!n) return 0;
  if (n == 1) return 1;
  if (kcache[k]) return kcache[k];
  LL s = F_sum(n);
  LL dec = 0;
  LL j;
  
  for (j = isqrt(n); j > 1; j--)
  {
    dec = (dec + j*retraction_sum((n/j)/j, k*j)) % mod;
  }
  
  LL res = (s - dec) % mod;
  if (res < 0) res += mod;
  kcache[k] = res;
  return res;  
}

LL slow_retraction_sum(LL n)
{
  LL * R = (LL*)malloc((CAP+1)*sizeof(LL));
  LL s = 1;
  LL i;
  for (i = 0; i <=n; i++) R[i] = 1LL;
  char * mask = (char *)malloc(n+1);
  memset(mask,1,n+1);
  
  for (i = 2LL; i <= n; i++)
  {
 //   printf("R[%llu]: %llu\n",i,R[i]);  
    if (mask[i])
    {
      LL p = i;
      while (p <= n)
      {
        LL j;
        for (j = p; j <=n; j += p)
        {
          if (p > i) R[j] /= (p/i + 1);
          R[j] *= p + 1;      
        }
        p *= i; 
      }
      
      LL k;
      for (k = 2*i; k <= n; k += i)
      {
        mask[k] = 0;
      }
    }
//    printf("R[%llu]: %llu\n",i,R[i]);
    s = (s + R[i]) % mod;
  }
  return s;
}


// sum i from 1 to n of floor(n/i)
LL G_sum(LL n)
{
    LL s = 0;
  LL m = 1;
  LL k = n;
  LL j;
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
    s = (s + (j+1)*k) % mod;
    m += j + 1;    
  }
  return s;
}

LL G_sum_slow(LL n)
{
  LL i;
  LL s = 0;
  for (i=1;i<=n;i++)
  {
    s = (s + (n/i)) % mod;
  }
  return s % mod;
}

// Sum of 1 over all (i,j) with i*j <= n and gcd(i,j) = 1
LL dec_sum(LL n,LL k)
{
  if (!n) return 0;
  if (n == 1) return 1;
  if (kcacheDec[k]) return kcacheDec[k];
  LL s = G_sum(n);
  LL dec = 0;
  LL j;
  
  for (j = isqrt(n); j > 1; j--)
  {
    dec = (dec + dec_sum((n/j)/j, k*j)) % mod;
  }
  
  LL res = (s - dec) % mod;
  if (res < 0) res += mod;
  kcacheDec[k] = res;
  return res;  
}

LL dec_sum_slow(LL n)
{
  LL * R = (LL*)malloc((CAP+1)*sizeof(LL));
  LL s = 1;
  LL i;
  for (i = 0; i <=n; i++) R[i] = 1LL;
  char * mask = (char *)malloc(n+1);
  memset(mask,1,n+1);
  
  for (i = 2LL; i <= n; i++)
  {
 //   printf("R[%llu]: %llu\n",i,R[i]);  
    if (mask[i])
    {
      R[i] = 2LL;
      
      LL k;
      for (k = 2*i; k <= n; k += i)
      {
        mask[k] = 0;
        R[k] *= 2LL;
      }
    }
//    printf("R[%llu]: %llu\n",i,R[i]);
    s = (s + R[i]) % mod;
  }
  return s;

}

int main()
{
  mod = 1000000007LL;
  sq = isqrt(CAP);
  printf("sq %lld\n",sq);
  kcache = (LL*)malloc((sq+1)*sizeof(LL));
  memset(kcache,0,(sq+1)*sizeof(LL));
  kcacheDec = (LL*)malloc((sq+1)*sizeof(LL));
  memset(kcacheDec,0,(sq+1)*sizeof(LL));
  
  LL tval = 2;
  LL diff = retraction_sum(tval,1LL) - dec_sum(tval,1LL);
  if (diff < 0) diff += mod;
  LL tval_mod = tval % mod;
  LL final_dec = ((tval_mod) * (tval_mod - 1) / 2) % mod;
  LL final_res = (diff - final_dec);
  if (final_res < 0) final_res += mod;
  printf("Number of retraction: %lld",final_res); 
//  printf("decSum(%lld): %lld\n",tval,dec_sum(tval,1LL));
 // printf("decSumSlow(%lld): %lld\n",tval,dec_sum_slow(tval));
  
//  printf("rSum(%lld): %lld\n",tval,retraction_sum(tval,1LL));
  //printf("rSumSlow(%lld): %lld\n",tval,slow_retraction_sum(tval));

}
