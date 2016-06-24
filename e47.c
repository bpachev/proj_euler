#include "primes.h"
#define CAP 1000000
#define NUMP P_UNDER_MILLION/5
#define NUM_FACTORS 4
#define NUM_CNC 4

int dist_pfactors(int n, int cap);
unsigned long long int * primes;

int main()
{
  int i;
  int last_was_good = 0;
  int curr_cnc = 0;
  char * mask = (char *)malloc(CAP/420);
   primes = (unsigned long long int *)malloc(sizeof(unsigned long long int)*NUMP);
  
  really_big_prime_mask_and_arr(mask, CAP/420, primes, NUMP);
  
  for (i = 2; i < CAP; i++)
  {
  //  printf("on %d\n",i);
    if (dist_pfactors(i, NUM_FACTORS))
    {
      if (last_was_good) curr_cnc++;
      else
      {
        curr_cnc = 1;
        last_was_good = 1;
      }
      
      if (curr_cnc == NUM_CNC)
      {
        printf("%d is the first number of a set of four to have four distinct prime factors.\n",i-NUM_CNC+1);
        break;
      }
    }
    else last_was_good = 0;
  }
}

int dist_pfactors(int n, int cap)
{
  int i = 0;
  int num_pfactors = 0;
  while (i < NUMP && primes[i] && primes[i] < n)
  {
    if (n % primes[i] == 0) 
    {
      num_pfactors++;
    }
    if (num_pfactors == cap) return 1;
    i++;
  }
  return 0;
}

