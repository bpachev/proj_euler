#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isPandigital(int n, int* mask);

int main()
{
  int mask[10];
  memset(mask, 0, sizeof(mask));
  mask[0] = 1; // no zeroes allowed.
  int i, k, j, l, m;
  int temp = 0; 
  long int sum = 0; 
  
  for (i=1;i < 10; i++)
  {
    mask[i] = 1;
    for (k=1; k < 10; k++)
    {
      if (mask[k]) continue;
      mask[k] = 1;
      for (j=1; j<10; j++)
      {
        if (mask[j]) continue;
        mask[j] = 1;
        for (l=1; l<10; l++)
        {
          if (mask[l]) continue;
          mask[l] = 1;
          for (m=1; m<10; m++)
          {
            if (mask[m]) continue;
            mask[m] = 1;
            temp = (i*10+k)*(j*100+l*10+m);
            if (isPandigital(temp,mask)) {sum += temp; printf("%d * %d = %d\n",(i*10+k),(j*100+l*10+m),temp);}
            temp = (i)*(k*1000 + j*100+l*10+m);
            if (isPandigital(temp,mask)) {sum += temp; printf("%d * %d = %d\n",(i),(k*1000 + j*100+l*10+m),temp);}
            mask[m] = 0;
          }

          mask[l] = 0;
        }

        mask[j] = 0;
      }
      mask[k] = 0;
      
    }
    mask[i] = 0;    
  }
  
  printf("Sum: %ld\n",sum);
}

int isPandigital(int n, int* mask)
{
  if (n >= 10000) return 0;
  int b, c, d,e;
  b = n / 1000;
  if (mask[b]) return 0;
  c = (n % 1000) / 100;
  if (mask[c]) return 0; 
  d = (n % 100) / 10;
  if (mask[d]) return 0;
  e = n % 10;
  if (mask[e]) return 0;
  
  if(b == c || b == d || b == e || c == d || c == e || d == e) return 0;
  return 1;  
}