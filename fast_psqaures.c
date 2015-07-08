#include "primes.h"
#define CAP 1125899906842624
#define NUMP 2063689
unsigned long long int * primes;
unsigned long long int * prime_squares;
unsigned long long int sum;

void print_psquares (unsigned long long int cap,unsigned long long int pnum, unsigned long long int prod)
{
//  printf("psquare %d\n",prod);
  sum++; 
  while(prime_squares[pnum] <= cap && prime_squares[pnum])
  {
    unsigned long long int curr_pow = 2;
    unsigned long long int accum = prime_squares[pnum];
    unsigned long long int curr_prime = primes[pnum];
    while(accum <= cap)
    {
      print_psquares(cap/accum,pnum+1,prod*accum);
      accum *= curr_prime;
    }
    pnum++;
  }
  return;
}

int main()
{
  char * mask = (char *)malloc(sqrt(CAP)/2);
  primes = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  prime_squares = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
  int i;
  sum = 0;
  
  really_big_prime_mask_and_arr(mask,sqrt(CAP)/2, primes,NUMP);
  
  for (i = 0; i < NUMP; i++) prime_squares[i] = primes[i]*primes[i];

  print_psquares(CAP, 0, 1);
  printf("There are %llu possible bases under %lu\n", sum-1,CAP);  
}