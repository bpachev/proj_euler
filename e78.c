#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#define CAP 1000000
#define MOD 1000000LL

long long int p[CAP+1];

long long int partitions(long long int n);

long long int partitions(long long int n)
{

  if (n < 0) return 0;
  if (p[n] != 0) return p[n];
  if (n == 1) return 1;
  long long int Pn = 0;
  long long int k,p1,p2;
  for (k = 1; k*k <= n; k++)
  {
    if (k*(3*k-1)/2 > n) break;
    if (k*(3*k +1)/2 > n)
    {
      p2 = 0;
      p1 = partitions(n - k*(3*k - 1)/2);
      if (k % 2 == 1) Pn += p1 + p2;
      else Pn = Pn - p1 - p2;
      if(Pn > 0) Pn = Pn;
      break;      
    }
    
    p1 = partitions(n - k*(3*k - 1)/2);
    p2 = partitions(n - k*(3*k +1)/2);
    
    if (k % 2 == 1) Pn += p1 + p2;
    else Pn = Pn - p1 - p2;
    Pn = Pn % MOD;    
  }
  p[n] = Pn;
  return Pn % MOD;
}


int main()
{
  memset(p,0,sizeof(p));  
  p[0] = 1;
  int i;
  for (i = 1; i < CAP; i++)
  {
    if (partitions(i) % MOD == 0) 
    {
      printf("%d\n",i);
      break;
    }
  } 
}