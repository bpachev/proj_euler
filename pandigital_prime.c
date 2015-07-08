#include "primes.h"
#define PRIME_CAP 2766
#define NUM_PRIMES 402
#define NUM_DIGITS 7

int main()
{
  char * mask = (char*)malloc(PRIME_CAP/2);
  int * primes = (int*)malloc(sizeof(int)*NUM_PRIMES);
  
  prime_mask_and_arr(mask,PRIME_CAP/2,primes,NUM_PRIMES);
  int d1,d2,d3,d4,d5,d6,d7;
  int marked[NUM_DIGITS+1];
  long int temp;
  memset(marked, 0, sizeof(marked));  
  
  for (d1 = NUM_DIGITS; d1 > 0; d1--)
  {
    marked[d1] = 1;
    for (d2 = NUM_DIGITS; d2 > 0; d2--)
    {
      if (marked[d2]) continue;
      marked[d2] = 1;
      for (d3 = NUM_DIGITS; d3 > 0; d3--)
      {
        if (marked[d3]) continue;
        marked[d3] = 1;
        for (d4 = NUM_DIGITS; d4 > 0; d4--)
        {
          if(marked[d4]) continue; 
          marked[d4] = 1;
          for (d5 = NUM_DIGITS; d5 > 0; d5--)
          {
            if(marked[d5]) continue;
            marked[d5] = 1;
            for (d6 = NUM_DIGITS; d6 > 0; d6--)
            {
              if(marked[d6]) continue;
              marked[d6] = 1;
              for (d7 = 1; d7 <= NUM_DIGITS; d7++)
              {
                if (marked[d7]||d7%2 == 0||d7 == 5) continue;
                temp  = d1*1000000 + d2*100000 + d3*10000 + d4*1000 + d5*100 + d6*10 + d7;
                if (faster_prime_check(temp,primes,NUM_PRIMES))
                {
                  printf("The biggest pandigital prime is: %ld\n",temp);
                  exit(1);
                }
              }
              marked[d6] = 0;
            }
            marked[d5] = 0;
          }
          marked[d4] = 0;
        }
        marked[d3] = 0;
      }
      marked[d2] = 0;
     }
     marked[d1] = 0;
  }
}