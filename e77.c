#include "primes.h"
#define CAP 100000
#define THRESH 5000
#define NUMP P_UNDER_MILLION

int main()
{
  int sofp[CAP+1];
  int i,j;  
  int p[CAP+1];
  unsigned long long int * primes = (unsigned long long int *)malloc(sizeof(unsigned long long int)*NUMP);
  char * mask = (char*)malloc(CAP/2);  
  if (!mask || ! primes)
  {
    fprintf(stderr,"Could not allocate memory.\n");
    exit(1);
  }
  for (i = 0; i <= CAP; i++)
  {
    sofp[i] = 0;
    p[i] = 0;
    //printf("%d\n",i);
  }
  really_big_prime_mask_and_arr(mask, CAP/2, primes, NUMP);
  
  for (i =0; i < NUMP && primes[i]; i++)
  {
    for (j = primes[i]; j <= CAP; j+=primes[i]) sofp[j] += primes[i]; 
  }
  
  for (i = 2; i <= CAP; i++)
  {
    p[i] = sofp[i];
    for (j = 1; j < i; j++) p[i] += p[i-j]*sofp[j];
    p[i] /= i;
    if (p[i] > 5000)
    {
      printf("%d\n",i);
      break;
    }
  }
}