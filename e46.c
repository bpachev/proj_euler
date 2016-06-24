#include "primes.h"
#define CAP 100000
#define NUMP CAP/6

int main()
{
  unsigned long long int i;
  char * mask = (char *)malloc(CAP/2);
  char * goldbach_mask = (char *)malloc(CAP/2);
  unsigned long long int * primes = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  unsigned long long int squares[(unsigned long long int)sqrt(CAP)]; 
  
//  printf("all mallocs worked\n");
  really_big_prime_mask_and_arr(mask,CAP/2,primes,NUMP);
  memset(goldbach_mask,1,CAP/2);
  for (i = 0; i < (unsigned long long int)sqrt(CAP); i++)
  {
    //printf("on square %d\n",i);
    squares[i] = i * i;
  }
  
  for (i = 1; i < NUMP && primes[i]; i++)
  {
    unsigned long long int j = 0;
    unsigned long long int tmp = primes[i];
    while (CONV_TO_MASK(2*squares[j] + tmp) < CAP/2) 
    {
   //   printf("%llu = 2*%llu + %llu\n",2*squares[j] + tmp,squares[j],tmp);
      goldbach_mask[CONV_TO_MASK(2*squares[j] + tmp)] = 0;
      j++;
    }
  }
  printf("checking for counter-examples\n");
  for (i = 0; i < CAP/2; i++) if(goldbach_mask[i]) printf("%llu breaks goldbachs other conjecture.\n",2*(i+1) + 1);
 // printf("%d\n",goldbach_mask[999/2-1]); 
}