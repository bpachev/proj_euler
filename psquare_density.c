#include "primes.h"
#define CAP 1000
#define NUMP P_UNDER_1000

int main()
{
  char * mask = (char *)malloc(CAP/2);
  int * primes = (int *)malloc(NUMP*sizeof(int));
  int * prime_squares = (int *)malloc(NUMP*sizeof(int));
  int i,j;
  int sum = 0;
  
  prime_mask_and_arr(mask,CAP/2, primes,NUMP);
  
  for (i = 0; i < NUMP; i++) prime_squares[i] = primes[i]*primes[i];
  
  for (i = 2; i <= CAP; i++)
  {
    register int inc = 1;
    for (j = 0; primes[j] && j < NUMP && primes[j] <= i; j++)
    {
      if (i % primes[j] == 0 && i % prime_squares[j] != 0)
      { 
        inc = 0;
        break;
      }
    }
    if (inc) printf("%d\n",i);
      
    sum += inc;
  }
  
  printf("There are %d numbers under %d that are potential bases.\n",sum,CAP);
}