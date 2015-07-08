#include "stdio.h"
#include "stdlib.h"

int main()
{
  unsigned long long int i;
  unsigned long long int pof10[20];
  pof10[0] = 1;
  for (i = 1; i < 20; i++) pof10[i] = 10*pof10[i-1];
  for (i = 1010101030; i < 1389026623;)
  {
    int j;
    unsigned long long int tmp = i*i;
    int is_good = 1;
    for (j = 1; j <= 8; j++)
    {
      if ((tmp%pof10[21-2*j]) / pof10[21-2*j-1] != j) {is_good = 0; break;}
    }
    if (is_good)
    {
      printf("%llu\n",i);
      break;
    }

    i += 40;

    tmp = i*i;
    is_good = 1;
    for (j = 1; j <= 8; j++)
    {
      if ((tmp%pof10[21-2*j]) / pof10[21-2*j-1] != j) {is_good = 0; break;}
    }
    if (is_good)
    {
      printf("%llu\n",i);
      break;
    }

    i += 60;    

  }
  
}
