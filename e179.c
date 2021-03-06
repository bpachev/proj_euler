#include "primes.h"
#define CAP 10000000
#define NUMP CAP/6

int main()
{
  char * mask = (char*)malloc(CAP/2);
  unsigned long long int * primes = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  
  long int num_cnc_dups = 0;
  really_big_prime_mask_and_arr(mask,CAP/2,primes,NUMP);
  int * div_mask = (int*)malloc(CAP*sizeof(int));
  long int i,j,k;
  for (i = 0; i < CAP; i++) div_mask[i] = 1;
  
  for (i = 0; i < NUMP && primes[i] < CAP && primes[i]; i++)
  {
    unsigned long long int currp = primes[i];
    unsigned long long int cumup = currp;
    for (j = 2; cumup < CAP; j++)
    {

      for (k = cumup-2; k < CAP-2; k+=cumup)
      {
        div_mask[k] *= j;        
        div_mask[k] /=  j-1;
      }
      cumup *= currp;
    }
  }
  
  for (i = 1; i < CAP-2; i++)
  {
    if (div_mask[i] == div_mask[i-1]) num_cnc_dups++;
  }  
   
  printf("There are %ld numbers less than %d that have the same number of divisors as their sucessor.\n",num_cnc_dups,CAP);
  free(mask);
  free(div_mask);

}