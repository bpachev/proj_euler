#include "primes.h"

#define NUMP 10
#define CAP 100

int main()
{
  int * primes = (int*)malloc(NUMP*sizeof(int));
  char * mask = (char*)malloc(CAP/2);
  prime_mask_and_arr(mask,CAP/2,primes,NUMP);
  int i;
  
  for(i = 0; i < 1 << NUMP; i++)
  {
    int accum = i;
    unsigned long long prod = 1;
    int num_primes = 0;
    
    while (accum)
    {
      if (accum & 1) prod *= primes[num_primes];
      accum >>= 1;
    }    
  }
}
