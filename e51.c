#include "primes.h"
#define CAP 1000000
#define NUMP CAP/6
#define THRESH 8
#define NUMD 6


int main()
{
  long int i,j,d1,d2,d3;
  char * mask = (char*)malloc(CAP/2);
  unsigned long long int * primes = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  int pof10[NUMD];  
  pof10[0] = 1;
  for (i = 1; i < NUMD; i++) pof10[i] = 10*pof10[i-1]; 
  
  really_big_prime_mask_and_arr(mask,CAP/2,primes,NUMP);
  
  int bm = 1;
  
  for (bm = 32; bm < 63; bm++)
  {
    int tmp = bm;
    long int inc = 0;
    int j = 0;
    int num_set = 0;
    char d_mask[NUMD];
    long int inc_mask[NUMD];
    for (i = 0; i < NUMD; i++)
    {
      if (tmp & 1)
      {
        num_set++;
        d_mask[i] = 1;
        inc_mask[j++] = pof10[NUMD-i-1];
      }
      
      else
      {
        inc += pof10[NUMD-i-1];
        d_mask[i] = 0;
      }
      tmp >>= 1;      
    }
    if (num_set != 3) continue;
    
    for (d1 = inc_mask[0]; d1 < 10*inc_mask[0]; d1+=inc_mask[0])
    {
      for (d2 = 0; d2 < 10*inc_mask[1]; d2 += inc_mask[1])
      {
        for (d3 = inc_mask[2]; d3 < 10*inc_mask[2]; d3 += 2*inc_mask[2])
        {
          int nump = 0;
          for (j = 0; j < 10; j++)
          {
            long int num = d1+d2+d3+j*inc;
            if (mask[CONV_TO_MASK(num)] && num > pof10[NUMD-1])
            {
              nump++;
            }
          }
          if (nump >= THRESH) printf("%ld\n",d1+d2+d3);
        }
      }
    }
    
  }
}