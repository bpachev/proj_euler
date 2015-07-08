#include "stdlib.h"
#include "stdio.h"
#include "string.h"

#define CAP 500000000
#define MAX_CACHE 1000000

unsigned long long int fast_tot_sum(unsigned long long int n);
unsigned long long int F_odd(unsigned long long int n);
unsigned long long int F(unsigned long long int n);
unsigned long long int fast_odd_tot_sum(unsigned long long int n);

unsigned long long int R[MAX_CACHE];


int main()
{
  memset(R,0,sizeof(R));
  printf("Sum: %llu\n",fast_odd_tot_sum(CAP-1) + 1);
}


//For algorithmic convenience, this function returns 1 less than the actual sum.
unsigned long long int fast_odd_tot_sum(unsigned long long int n)
{
  if (n == 1) return 0;
  if (n < MAX_CACHE) {
    if (R[n]) return R[n];
  }

  unsigned long long int s = F_odd(n);
  unsigned long long int k = n/2;
  unsigned long long int m = 2;
  unsigned long long int j;
  
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
    //printf("k %llu j %llu m %llu\n",k,j,m);
    if (m % 2 == 0) s -= ((j+1)/2) * fast_odd_tot_sum(k);
    else s -= (1 + (j/2)) * fast_odd_tot_sum(k);
    m += j + 1;
  }
  if (n < MAX_CACHE) R[n] = s;
  return s;
}

unsigned long long int fast_tot_sum(unsigned long long int n)
{
  if (n == 1) return 0;
  if (n < MAX_CACHE) {
    if (R[n]) return R[n];
  }

  unsigned long long int s = F(n);
  unsigned long long int k = n/2;
  unsigned long long int m = 2;
  unsigned long long int j;
  
  while (k > 1)
  {
    k = n / m;   
    j = (n % m) / k;
//    printf("k %llu j %llu m %llu\n",k,j,m);
    s -= (j+1) * fast_tot_sum(k);
    m += j + 1;
  }
  if (n < MAX_CACHE) R[n] = s;
  return s;
}

unsigned long long int F(unsigned long long int n)
{
  return n * (n - 1)/2;
}


unsigned long long int F_odd(unsigned long long int n)
{
  unsigned long long int d = (n-1) / 2;
  return d * (d + 1);
}

