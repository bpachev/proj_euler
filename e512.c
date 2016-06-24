#include "primes.h"

#define CAP (100 - 2)

int main()
{
  int i;
  unsigned long long int sum = 1;
  char * mask = (char *)malloc(CAP/2);
  int * tot = (int *)malloc((CAP/2)*sizeof(int));
  tot_fill(mask, CAP/2, tot);

  for (i = 0; i < CAP/2; i++) {
    sum += tot[i];
    printf("tot(%d) = %d\n",1 + 2*(i+1),tot[i]);
  }
  printf("Sum %llu\n",sum);
}
