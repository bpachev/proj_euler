//Benjamin Pachev May 2015


#include "primes.h"
//#define CAP (5000000000000000LL)
#define CAP 5000000LL
#define MASK_SIZE (((int)(sqrt(CAP)/2)) + 1000)
#define NUMP 600
//#define NUMP (4157407LL)
//#define NUMP 4

unsigned long long int arithmetic_derivative(unsigned long long int n, unsigned long long p_num);
unsigned long long int num_admissible(unsigned long long int n, unsigned long long int p_max);

char* mask;
unsigned long long int * primes;



int main()
{
  int i;
  mask = (char*)malloc(MASK_SIZE);
  primes = (unsigned long long int *)malloc(NUMP*sizeof(unsigned long long int));
 // printf("Memory trouble over, seg-fault probably due to out-of-bounds access.\n");
  really_big_prime_mask_and_arr(mask,MASK_SIZE,primes, NUMP);
  //printf("Prime sieve successful. The error is in the new code.\n");
  for (i = 0; i < 2; i++) printf("n:%lld sum: %llu\n",CAP+i,arithmetic_derivative(CAP+i,0) - 1);
}

//Returns the number of natural numbers <= n that are not divisible by any prime before the p_max-th prime.
//If p_max = pi(sqrt(n)), then this counts the number of primes > sqrt(n) and <=n.
unsigned long long int num_admissible(unsigned long long int n, unsigned long long int p_max)
{
  unsigned long long int dec = 0;
  unsigned long long int i = 0;
  while ((i < p_max) && (primes[i] <= n))  {
    dec += num_admissible(n/primes[i],i);
    i++;
  }  
  return n - dec;
  
}


//Returns the sum from k = 1 to n of gcd(k, k'), where k' is defined by the Leibniz rule for composite k
// (i.e. (ab)' = a'b + b'a).
// p' = 1 for all prime p. (btw 1' = 0, which isn't hard to prove)
//n is the absolute upper bound. p_num is the current prime index.
unsigned long long int arithmetic_derivative(unsigned long long int n, unsigned long long p_num)
{
 // printf("Called with n = %llu, p_num = %llu\n",n,p_num);
  unsigned long long int pow = 0;
  unsigned long long int accum = 1;
  unsigned long long int sum = 0;
  if (p_num >= NUMP) {
   // printf("Only %d primes\n",NUMP);
    //printf("Returned %llu\n",num_admissible(n,p_num));
    return num_admissible(n,p_num);
  }
  register int p = primes[p_num];
  if (!n) return 0;
  if (n == 1) return 1;
  if (p*p > n) return  num_admissible(n,p_num);

  while (accum <= n) {
    if (pow == p) {
      //everything divisible by p^p OR a higher power of p
      sum += accum*arithmetic_derivative(n/accum,p_num);
      return sum;
    }

    //everything divisible by EXACTLY p^pow
    else if (pow) sum += (accum/p)*arithmetic_derivative(n/accum,p_num + 1);

    //everything 
    else sum += arithmetic_derivative(n/accum,p_num + 1);

    pow++;
    accum *= p;
  }
  return sum;
}



