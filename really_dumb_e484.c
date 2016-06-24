#include "stdio.h"
#include "stdlib.h"
#define CAP 5000000000000000LL
#define STOP CAP
#define START CAP-1000000+1

unsigned long long int gcd(unsigned long long int a, unsigned long long int b);
unsigned long long int kprime(unsigned long long int k)
{
  if (k <= 1) return 0;
  unsigned long long int j;
  for (j = 2; j*j <= k; j++)
  {
    if (k % j == 0) return kprime(k/j)*j + (k/j)*kprime(j);
  }
  return 1;
}

unsigned long long int gcd(unsigned long long int a, unsigned long long int b)
{
  if (b == 0) return a;
  else return gcd(b,a%b);
}


int main()
{
  unsigned long long int sum = 0;
  unsigned long long i;
  for (i = START; i <= STOP; i++) {sum += gcd(i, kprime(i)); }
  printf("sum from %llu to %llu: %llu\n",START,STOP,sum);
 // printf("%llu",kprime(20));
}