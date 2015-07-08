#include "math.h"
#include "stdio.h"
#include "stdlib.h"
#define CAP 50000

int is_triangular(unsigned long long int n);
int is_pentagonal(unsigned long long int n);

int is_triangular(unsigned long long int n)
{
  unsigned long long int tmp = 8*n + 1;
  unsigned long long int sq = sqrt(tmp);
  if (sq * sq == tmp)
  {
    if ((sq - 1) % 2 == 0) return 1;
    else return 0;
  }
  else if ((sq+1)*(sq+1) == tmp)
  {
    if ((sq) % 2 == 0) return 1;    
    else return 0;
  }
  else if ((sq-1)*(sq-1) == tmp)
  {
    if ((sq - 2) % 2 == 0) return 1;
    else return 0;    
  }  
  else return 0;
} 

int is_pentagonal(unsigned long long int n)
{
  unsigned long long int tmp = 1 + 24*n;
  unsigned long long int sq = sqrt(tmp);
  if (sq * sq == tmp)
  {
    if ((sq + 1) % 6 == 0) return 1;
    else return 0;
  }
  else if ((sq+1)*(sq+1) == tmp)
  {
    if ((sq + 2) % 6 == 0) return 1;    
    else return 0;
  }
  else if ((sq-1)*(sq-1) == tmp)
  {
    if ((sq) % 6 == 0) return 1;
    else return 0;    
  }  
  else return 0;
}


int main()
{
  
  unsigned long long int i = 0;
  while (i < CAP)
  {
    unsigned long long int tmp = i*(2*i - 1);
    if (is_pentagonal(tmp) && is_triangular(tmp))
    {
      printf("%llu %llu is a triangular number that is pentagonal and hexagonal.\n",tmp, i);
    }
    i++;
  }
}