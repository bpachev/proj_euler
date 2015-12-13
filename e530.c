#include "proj_euler.h"

//#define CAP 100000000000000LL
#define CAP 1000000000000000LL

LL sq;
LL * kcacheDec;

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
    s = (s + (j+1)*k);
    m += j + 1;    
  }
  return s;
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
    dec = (dec + dec_sum((n/j)/j, k*j));
  }
  
  LL res = (s - dec);
//  if (res < 0) res += mod;
  kcacheDec[k] = res;
  return res;  
}

int main()
{
  int i;
  sq = isqrt(CAP);
  kcacheDec = (LL*)malloc((sq+1)*sizeof(LL));
  memset(kcacheDec,0,(sq+1)*sizeof(LL));
  LL sum = 0;
  dec_sum(CAP,1);
  for (i=1; i <= sq; i++)
  {
    sum += i*dec_sum(CAP/i/i,i);
  }
  printf("Sum %lld\n",sum); 
}
