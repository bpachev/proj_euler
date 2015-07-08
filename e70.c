#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CAP 10000000

int is_permu(int a, int b);

int is_permu(int a, int b)
{
  int a_digits[10];
  int b_digits[10];
  int i;
  for (i=0; i < 10; i++)
  {
    a_digits[i] = 0;
    b_digits[i] = 0;
  }
  
  while (a)
  {
    a_digits[a%10]++;
    a /= 10;
  }
  
  while (b)
  {
    b_digits[b%10]++;
    b /= 10;
  }

  for (i = 0; i < 10; i++)
  {
    if (a_digits[i] != b_digits[i]) return 0;
  }
  
  return 1;
}


int main()
{
  printf("is_permu(12340,40312)%d\n",is_permu(12340,40312));

  int i;  
  char * mask = malloc(CAP);
  int * tot = malloc(CAP*sizeof(int));
  float min = (float)CAP;
  int minimizer = 0;
  memset (mask,1,CAP);
  for (i=0;i<CAP;i++)
  {
    tot[i] = i;
  }

  for (i=2;i<CAP;i++)
  {
    int inc = i;
    if (mask[i] == 1)
    {
      int j;
      tot[i]--; //tot(p) = p-1 for p prime.
      for (j = i+inc;j<CAP;)
      {
        mask[j] = 0;
        tot[j] = tot[j] - (tot[j] / inc);
        j += inc;
      } 
    }
    
    if (is_permu(i,tot[i]))
    {
      float temp = ((float)i)/tot[i];
      if (temp < min)
      {
        min = temp;
        minimizer = i;
      }
    }
  }
  
  printf("Solution: %d\n",minimizer);

}



