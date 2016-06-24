#include "primes.h"
#define CAP 1000000
#define SOL_CAP 1000
#define PCAP P_UNDER_MILLION
#define POW_CAP 9

int * primes;

unsigned long long int diophantine_solutions(unsigned long long int n);

unsigned long long int diophantine_solutions(unsigned long long int n)
{
  unsigned long long int num_solns = 0;
  unsigned long long int k;
  for (k = n + 1; k <= 2*n; k++)
  {
    if (k*n % (k - n) == 0)
    { 
      num_solns++;
//      printf("1/%d + 1/%d = 1/%d.\n",k,k*n/(k-n),n);
    }
  }
  return num_solns;
}

unsigned long long int pf_diophantine(unsigned long long int n);


unsigned long long int pf_diophantine(unsigned long long int n)
{ 
  int i = 0;
  unsigned long long int m = n;
  int prod = 1;
  int tmp = primes[i];
  register int exp = 0;
  while (tmp  <= n/2)
  {
    while (m % tmp == 0)
    {
      m /= tmp;
      exp++;
    }
    prod *= (2*exp+1);
    if (m == 1) return prod/2 + 1; 
    exp = 0;
    i++;
    tmp = primes[i];
  }
  return prod/2 + 1;
}

int main()
{
  unsigned long long int i = 2;
  unsigned long long int tmp = diophantine_solutions(i);
  primes = (int*)malloc(PCAP*sizeof(int));
  char * mask = (char*)malloc(CAP/2);
  prime_mask_and_arr(mask, CAP/2, primes, PCAP);
  free(mask);

  printf(" %llu\n" ,diophantine_solutions(3620778609848384));
  
  while (tmp <= SOL_CAP && i < CAP)
  {
    i++; 
    tmp = pf_diophantine(i);
  }
  printf("%llu is the first integer to have over %d solutions, with %llu solutions.\n",i,CAP,diophantine_solutions(i));  
}