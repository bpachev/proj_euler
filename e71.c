#include "stdio.h"
#include "stdlib.h"
#define CAP 1000000

int gcd(int a, int b);

int gcd(int a, int b)
{
  if (b == 0) return a;
  else return gcd(b,a%b);
}


int main()
{
  int i,f,h;

  printf("%d\n",7*(CAP/7));  
}