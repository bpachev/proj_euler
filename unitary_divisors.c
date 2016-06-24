#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//computes the sum of the squares of the unitary divisors of n! modulo mod, where n is CAP

#define CAP 100000000
//#define CAP 62991251
//#define CAP 10

unsigned long long int mod_pow(unsigned long long int base, unsigned long long int exp,unsigned long long int mod);


unsigned long long int mod_pow(unsigned long long int base, unsigned long long int exp, unsigned long long int mod)
{
    unsigned long long int result = 1;
    while (exp)
    {
        if (exp % 2) 
        {
          result = (result * base) % mod;
        }
        exp = exp / 2;
        base = (base * base) % mod;
    }

    return result;
}


int main()
{
  unsigned long long int i;
  char * mask = (char*)malloc(CAP/2);
  if (!mask)
  {
    printf("Memory Error\n");
  }
  
  memset(mask,1,CAP/2);
  unsigned long long int mod = 1000000009;
  unsigned long long int accum = 1;
  unsigned long long int pow = 0;
  unsigned long long int b2 = 2;
  
  for (i=b2;i<=CAP;i*=b2) pow += CAP/i;
  accum = (accum * (1 + mod_pow(b2,2*pow,mod))) % mod;
  
    
  for (i=0;i<CAP/2;i++)
  {
    unsigned long long int inc = 2*(i + 1) + 1;
    if (inc > CAP) break;
    if (mask[i])
    {
      unsigned long long int j,p;
      pow = 0;
      
      for (p=inc;p<=CAP;p*=inc) pow += CAP/p;
      //printf("%llu %d %llu\n",pow,inc,mod_pow(inc,2*pow,mod));
      accum = (accum * (1 + mod_pow(inc,2*pow,mod))) % mod;
      //printf("%d\n",inc);
      
      for (j = i+inc;j<CAP/2;)
      {
        mask[j] = 0;
        j += inc;
      } 
    }
  }
  printf("The sum of squares of unitary divisors of %d! = %llu\n",CAP,accum);
  return 0; 
}
