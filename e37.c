#include "primes.h"
#define CAP 1000000


int pows[5];

int is_truncable(int p,char * mask);


int is_truncable(int p,char * mask)
{
  int i;
  int n = (int)log10(p);
  int d;
  int m;
  for (i = 0; i < n; i++)
  {
    m = p % pows[i];
    d = p / pows[i];
    if (m < 2 || d < 2) return 0;
    if (m != 2 && !MASK_WITH_CHECK(m,mask)) return 0; 
    if (d != 2 && !MASK_WITH_CHECK(d,mask)) return 0;
  }
  
  return 1;
}

int main()
{
  char * mask = malloc(CAP/2);
  int * primes = malloc(sizeof(int)*P_UNDER_MILLION);
  
  prime_mask_and_arr(mask, CAP/2, primes, P_UNDER_MILLION);
  register int i;
  long int sum = 0;
  
  pows[0] = 10;
  for (i=1; i<5; i++)
  {
    pows[i] = 10*pows[i-1];
  }
  
  // we start i at 4 to avoid the single digit primes 2, 3, 5, and 7
  for (i = 4; i < P_UNDER_MILLION; i++)
  {
    if (is_truncable(primes[i],mask))
    {
      sum += primes[i];
    }
  } 
  
  printf("Sum: %ld\n",sum);
}