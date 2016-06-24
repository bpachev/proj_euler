#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
//#define CAP 28132
#define CAP 20162
#define AB_CAP 10000

long int d(int x);

int main()
{
 int mask[CAP];
 int ab_nums[AB_CAP];
 int curr_ind = 0;
 long int i;
 unsigned long long int sum; 
 memset(mask,0,sizeof(mask));
 
 for (i = 0; i < CAP; i++)
 {
   if (d(i) > i)
   {
     ab_nums[curr_ind++] = i;
     int j;
     for (j = 0; j < curr_ind; j++)
     {
       long int s = i + ab_nums[j];
       if (s < CAP) mask[s] = 1;
     }
   }
   
   if (!mask[i]) sum += i;
 }
 
 printf("Sum: %llu\n",sum);
// printf("d(900) %ld\n",d(12));
}

long int d(int x)
{
  if (x < 2) return 0; 
  long int sum = 1;
  int sq = (int)sqrt(x);
  if (sq == 1) return 1;
  int i;
  for (i = 2; i < sq; i++)
  {
    int mod = x % i;
    int div = x / i;
    if (mod == 0)
    {
      sum += i + div;
    }    
  }
  
  if (sq*sq == x) sum += sq;
  else if (x % sq == 0) sum += sq + x / sq;
  return sum;
}