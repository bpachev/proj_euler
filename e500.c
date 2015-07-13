#include "primes.h"

#define CAP 8000000
#define NUMP 500500

typedef unsigned long long int ULL;

ULL mod_pow(ULL base, ULL exp,ULL mod);


ULL mod_pow(ULL base, ULL exp, ULL mod)
{
    ULL result = 1;
    while (exp)
    {
        if (exp % 2) 
        {
          result = (result * base) % mod;
        }
        exp = exp / 2;
        base = (base * base) % mod;
    }

    return result;
}


int main()
{
  long long int i,j;
  ULL mod = 500500507LL;
  ULL accum = 1;
  ULL * exps = (ULL*)malloc(NUMP*sizeof(ULL));
  memset(exps,0,NUMP*sizeof(ULL));
  char * mask = (char*)malloc(CAP/2);
  ULL * primes = (ULL*)malloc(NUMP*sizeof(ULL));
  
  really_big_prime_mask_and_arr(mask,CAP/2,primes,NUMP);
  float l2 = log(2);
  ULL curr_len = 0;
  for (i = 2; i <= NUMP; i++)
  {
    cand = primes[curr_len];
    cand_objective = log(log(cand));
    for (j = curr_len - 1; j >= 0; j--)
    {
      float temp_obj = log(log(primes[j])) + (exp[j])*l2;
      if (temp_obj < cand_objective)
      {
        cand_objective = temp_obj;
        cand = j;
      }
    }
    if (cand == curr_len) curr_len++;
//    accum = 
  }
  
}
