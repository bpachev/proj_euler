#include "primes.h"
#define CAP 1000000
#define THRESH 10000000000
#define NUMP P_UNDER_MILLION

int main()
{
  unsigned long long int* primes = (unsigned long long int *)malloc(sizeof(unsigned long long int)*NUMP);
  char * mask = (char*)malloc(CAP/2);
  really_big_prime_mask_and_arr(mask, CAP/2, primes, (unsigned long long int)NUMP);
  
  unsigned long long int i;
  for (i = 0; i < NUMP; i += 2)
  {
    if (2*primes[i]*(i + 1)  > THRESH)
    {
      printf("Prime: %llu, num: %llu\n",primes[i],i+1);
      break;
    }
  }
}