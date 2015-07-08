#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long int LL;
#define CAP 1000000000000000LL
//#define CAP 1000000LL
//#define MOD_SQ_SUM(n) ((((((((n)*(n+1) % mod) * (2*n+1)) % mod) / 2) * (inv3) % mod))%mod)

LL mod;
LL inv3;

LL mod_sq_sum(LL n)
{
  LL res = 1;
  LL t1,t2,t3;
  t1 = n;
  t2 = n+1;
  t3 = 2*n+1;
  
  if (n %2 == 0)
  {
    t1 = t1/2;
  }
  else
  {
    t2 = t2 / 2;  
  }
  
  switch (n%3)
  {
    case 0:
      t1 /=3;
      break;
    case 1:
      t3 /= 3;
      break;
    default:
      t2/=3;
      break;
  }
  
  res = (res*(t1%mod)) % mod;
  res = (res*(t2%mod)) % mod;
  res = (res*(t3%mod)) % mod;
  return res; 
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
    LL j_t = (m+j ) % mod;
    LL m_t = m % mod;
    LL coeff = (mod_sq_sum(j_t) - mod_sq_sum((m_t-1)))%mod;
    while (coeff < 0) coeff += mod;
//    printf("m %lld k %lld coeff %lld j%lld, sum m-1 %lld\n",m,k,coeff,j,MOD_SQ_SUM((m-1)));
    s = (s + coeff*(k%mod)) % mod;
    m += j + 1;    
  }
  return s % mod;
}

 // sum i=1 to i=n i*floor(n/i) modulo mod
LL F_sum_slow(LL n)
{
  LL s = 0;
  LL i;
  for (i = 1; i <= n; i++)
  {
    LL i_t = i % mod;
    s = (s + ((i_t*i_t) % mod) * ((n/i) % mod)) % mod;
  }
  return s;
}


int main()
{
  mod = 1000000000LL;
  inv3 = 666666667LL; // 3 inverse modulo mod
  LL n = CAP;
  printf("sum: %lld \n",F_sum(n));
 // printf("sumSlow: %lld\n",F_sum_slow(n));
}
