#include "stdlib.h"
#include "stdio.h"
#define NUM_DIGITS 100

unsigned long long int fact[11];
unsigned long long int ncr(int n, int r);

int main()
{
  fact[0] = 1;
  unsigned long long int sum = 9;
  int i;
  for (i=1;i<10;i++) fact[i] = i*fact[i-1];  
  for(i = 2; i <= NUM_DIGITS; i++)
  {
    sum += ncr(8+i,8) + ncr(9+i,9) - 10;
  }
  printf("There are %llu nonbouncy numbers with %d digits.\n",sum,NUM_DIGITS);
}

unsigned long long int ncr(int n, int r)
{
  unsigned long long int prod = 1;
  int i;
  for (i=0; i < r; i++) prod *= (n-i);
  return prod/fact[r];
}