#include "primes.h"

#define CAP 100000000LL
#define MAX_ITER sqrt(CAP)


int main()
{
  // Find the sum of all integers 0 < n =< CAP such that for all divisors d of n, d + n/d is prime. 
  char* mask = (char*)malloc(CAP/2);
  char* mask2 = (char*)malloc(CAP/2);
  memset(mask2,1,CAP/2);
  big_prime_mask(mask,CAP/2);
  unsigned long long int sum = 1; //1 should be counted in the sum since 1 + 1/1 = 2 is prime. All other odds fail.
  int i,j;
  for (i = 1; i < MAX_ITER; i++)
  {
    for (j = 1 + i%2; i*j < CAP; j+=2) //ensure they'll be of opposite parity
    {
    //  printf("i %d j %d\n",i,j);
      if (!mask[CONV_TO_MASK(i+j)])
      {
        mask2[i*j/2] = 0;
      }
    }
  }
  
  for (i = 1; i < CAP/2; i++)
  {
    if (i%2 == 0) continue;
    if (mask2[i]) 
    {
      //printf("prime generator n: %d\n",2*i);
      sum += 2*i;
    }
  }
  printf("Sum %llu\n",sum);
}
