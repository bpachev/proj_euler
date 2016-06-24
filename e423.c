#include "proj_euler.h"
#define CAP 50000000LL
#define MOD 1000000007LL

int main()
{
  char * mask = (char*)malloc((CAP+1));
  memset(mask,1,CAP+1);
  LL i,j;
  LL s = 6LL; //count n = 1
  LL p = 0LL; //number of primes
  LL C = 6LL; //C(n) C(1) = 6
  LL err = 6LL; //Error correcting term = 6*5^(n-1-pi(n))*(n -1 choose pi(n)) (pi = prime counting function). Needs to be subtracted from the total at each step 
  for (i = 2; i <= CAP; i++)
  {
    if (i % 1000000LL == 0) printf("On %lld\n",i);
    C = (6*C - err) % MOD;
  
    if (mask[i])
    {
      p++;
//      err = (5*err) % MOD;
      err = (err*(i-1LL)) % MOD;
      err = (err*smod_pow(p,MOD-2LL,MOD)) % MOD;
      C = (C + err) % MOD;
      if (i <= CAP/i) //prevent overflow. Checking i*i < cap can yield invalid results for i > 4*10^9
      {
        for (j = i*i; j <= CAP; j += i)
        {
          mask[j] = 0;
        }
      }
    }
    
    else 
    {
      err = (5LL*err) % MOD;
      err = (err*(i-1LL)) % MOD;
      err = (err * smod_pow(i-p-1LL,MOD-2LL,MOD)) % MOD;
    }
    while (C < 0) C += MOD;
    
//    printf("C(%lld) = %lld\n",i,C);
    s = (s + C) % MOD;
  }
  
  printf("S(%lld) mod %lld = %lld\n",CAP,MOD,s);
  
}
