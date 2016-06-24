#include <stdio.h>
#include <stdlib.h>

int main()
{
  int i, j, k, l;
  int num = 0;
  int den = 0;
  
  // kl/ij is the fraction being considered.
  
  for (i = 1; i < 10; i++)
  {
    for (j = 1; j < 10; j++)
    {
      for (k = 1; k <= i; k++)
      {
        for (l = 0; l < 10; l++)
        {          
          if (i == k && l < j)
          {
            num = k*10 + l;
            den = i*10 + j;
            if ((float)num/den == (float)l/j) printf("%d/%d = %d/%d\n",num,den,l,j);
            continue;
          }
          
          if (i == l && j != k)
          {
            num = k*10 + l;
            den = i*10 + j;
            if ((float)num/den == (float)k/j) printf("%d/%d = %d/%d\n",num,den,k,j);
            continue;            
          }
          
          
        }
      }
    }
  }
}