#include "stdlib.h"
#include "stdio.h"

#define maxDigits 9

int p10[maxDigits];

int rev(int n,int d)
{
  if (n%10 == 0) return 0;
  int t = n;
  int i = 0;
  int r = 0;
  while (t)
  {
    r += (t%10)*(p10[i] + p10[d-i]);
    t /= 10;
    i += 1;
  }
  while (r)
  {
    if (r%2 == 0)
    {
      return 0;
    }
    
    r /= 10;
  }
//  printf("r %d, n %d, d %d\n",r,n,d);  
  return 1;
}

int main()
{
  int j,i;
  int s = 0;
  
  p10[0] = 1;
  for (i=1;i<maxDigits;i++)
  {
    p10[i] = 10*p10[i-1];    
  } 

  for (i = 0; i < maxDigits; i++)
  {
    for (j = p10[i]; j < 10*p10[i]; j++)
    {
      s += rev(j,i);
    }
  }
  printf("Reversible numbers below 10^%d %d\n",maxDigits,s);
}
