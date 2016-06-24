#include <stdio.h>
#include <stdlib.h>

int main()
{
  int f[10]; // factorials
  f[0] = 1;
  int i,j,k,l,m,n;
  long int sum = 0;
  int temp;
  int t2;
  for (i = 1; i < 10; i++)
  {
    f[i] = i*f[i-1];
//    printf("%d factorial = %d\n",i,f[i]); 
  }
//  f[0] = 0;  
  
  for (i = 0; i < 10; i++)
  {
    for (j = 0; j < 10; j++)
    {
      for (k = 0; k < 10; k++)
      {
        for (l = 0; l < 10; l++)
        {
          for (m = 0; m < 10; m++)
          {
            for (n = 0; n < 10; n++)
            {
              temp = i*100000 + j*10000 + k*1000 + l*100 + m*10 + n;
              if (i) t2 = f[i] + f[j] + f[k] + f[l] + f[m] + f[n];
              else if (j) t2 = f[j] + f[k] + f[l] + f[m] + f[n];
              else if (k) t2 = f[k] + f[l] + f[m] + f[n];
              else if (l) t2 = f[l] + f[m] + f[n];
              else if (m) t2 = f[m] + f[n];
              else  t2 = 0;
              if (temp == t2)
              {
                sum += temp;
 //               printf("%d\n",temp);
              }
            }
          }
        }
      }
    }
  }
  
  printf("sum: %ld\n",sum);
  
}