#include "primes.h"
#define CAP 12221
#define NUM_PRIMES sqrt(CAP)/2

unsigned long long int gcd_k_kprime(int k);

int * primes;
int * prime_squares;

unsigned long long int gcd_k_kprime(int k)
{
  register int j;
  register int exp = 0;
  register int tmp;
  unsigned long long int prod = 1;
  for (j = 0; j < NUM_PRIMES && primes[j]; j++)
  {
    exp = 0;
    tmp = prime_squares[j];
    if (k  % prime_squares[j] == 0)
    {
      exp += 2;
      k /= tmp;
      tmp = primes[j];
      prod *= tmp;
      while (k % tmp == 0)
      {
        k /= tmp;
        prod *= tmp;
        exp++;
      }
      
      if (exp % tmp == 0) prod *= tmp;
    }
  }
  
  return prod;
}


int main()
{
  register int i;
  char * mask = malloc(sqrt(CAP)/2);
  primes = malloc(NUM_PRIMES*sizeof(int));
  prime_squares = malloc(NUM_PRIMES*sizeof(int));
  prime_mask_and_arr(mask, sqrt(CAP)/2,primes, NUM_PRIMES);
  for (i = 0; i < NUM_PRIMES; i++)
  {
    prime_squares[i] = primes[i]*primes[i];
  }
  unsigned long long int sum = 0; 
  
 // printf("gcd(20,(20)') = %llu\n",gcd_k_kprime(90,primes,prime_squares));
  
  for (i = 2; i <= CAP; i++)
  {
    sum += gcd_k_kprime(i);
  }
  
  printf("Sum: %llu\n",sum);
}