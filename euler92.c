#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ONE 1
#define EIGHTY_NINE 2
#define CAP 568
#define MAX_NUM 10000000

int terminal_num(long int n);
int mask[CAP];
int squares[10];


int terminal_num(long int n)
{
  if (n < CAP) 
  {
    register int sum = 0;
    register int d = mask[n];    
    if (d) return d;    
    if (n == ONE) return ONE;
    if (n == 89) return EIGHTY_NINE;
    while (n)
    {
      d = n % 10;
      sum += d*d;
      n /= 10;
    }
    d = terminal_num(sum);
    mask[n] = d;
    return d;
  }
  
  else
  {
    register int sum = 0;
    register int d;
    while (n)
    {
      d = n % 10;
      sum += squares[d];
      n /= 10;
    }
    return terminal_num(sum);  
  }
}

int main()
{
  memset (mask, 0, sizeof(mask));
  register int i;
  register long int s = 0;

  for (i = 1; i <= 10; i++) squares[i] = i*i;
  
  for (i = 1; i < MAX_NUM; i++)
  {
    if (terminal_num(i) == EIGHTY_NINE)
    {
      s++;
    }
  }
  
  printf("There are %ld starting numbers which end in 89.\n",s);  
}