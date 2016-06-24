#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define CAP 1000
enum {FZERO=0,SZERO,ONE};


int len_unit_cycle(int x);

int main()
{
  int i = 0;
  int max = 0;
  int curr = 0;
  int mnum = 0;
  for (i = 101; i < 1000; i++)
  {    
    curr = len_unit_cycle(i);
 //   if (curr == -1) printf("Exceeded cap on iter %d\n", i);
    if (curr >= max)
    {
   //   printf("Updating max from %d to %d on iter %d\n",max,curr,i);
      mnum = i;
      max = curr;
    }
  }
  
  printf("The number with the longest period was %d with a period of %d\n",mnum,max);
//  printf("\n%d\n",len_unit_cycle(727));
}

int len_unit_cycle(int x)
{
  unsigned long long int numer = 10;
  int d;
  int i;
  int pos[10];
  memset(pos, 0, sizeof(pos));
  int STATE = -1;
  
//  printf("\n1/%d = ",x);
  for (i = 0; i < CAP; i++)
  {
    d = numer / x;
    numer = 10 * (numer % x);
    if (STATE < 1 && d == 0) 
    {
      //printf("state before 0 %d\n",STATE);      
      STATE++;
    //  printf("state after 0 %d\n",STATE);
      continue;
    }
  //  printf("digit: %d\n",d);
  //  if (d == 1) printf("state: %d, ", STATE);
    if (d == 1 && STATE == SZERO && i > 3) return i - 2;
    else STATE = -1;
  }  
//  printf("\n");
  return -1;
}

