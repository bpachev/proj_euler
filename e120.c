#include "stdio.h"
#include "stdlib.h"
#define CAP 1000


int main()
{
  int i;
  int sum = 0;
  for (i = 3; i <= CAP; i++)
  {
    sum += i * ( 2 * ((i-1)/2));
  }
  printf("sum: %d\n",sum);
}