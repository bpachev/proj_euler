#include "primes.h"
#define CAP 10000
#define NUMP 1229 

char * mask;
int * primes;
int prime_permus(int p);
int permus_of_four[24][4];

int main()
{
  int d1,d2,d3,d4;
  int marked[4];
  int row = 0;
  memset(marked, 0, 4*sizeof(int));
  for (d1 = 0; d1 < 4; d1++)
  {
    marked[d1] = 1;
    for (d2 = 0; d2 < 4; d2++)
    {
      if (marked[d2]) continue;
      marked[d2] = 1;
      for (d3 = 0; d3 < 4; d3++)
      {
        if (marked[d3]) continue;
        marked[d3] = 1;
        for (d4 =0; d4 < 4; d4++)
        {
          if (marked[d4]) continue;
          permus_of_four[row][0] = d1;
          permus_of_four[row][1] = d2;
          permus_of_four[row][2] = d3;
          permus_of_four[row][3] = d4;
          row++;
        }
        marked[d3] = 0;
      }
      marked[d2] = 0;
    }
    marked[d1] = 0;
  }
  
  int i;
  mask = (char *)malloc(CAP/2);
  primes = (int *)malloc(CAP/2);
  prime_mask_and_arr(mask, CAP,primes,NUMP);
  
  for (i = P_UNDER_1000; i < NUMP; i++)
  {
    int already_seen = mask[CONV_TO_MASK(primes[i])];
    int tmp = prime_permus(primes[i]);
    if(tmp >= 2 && already_seen) printf("%d has at least 3 prime permutations, with %d permutations.\n",primes[i],tmp);
  }
  
}

int prime_permus(int p)
{
  int d[4];
  int permus[24];
  memset(permus,0,sizeof(permus));
  int i = 0;
  int num_pp = 0;
  d[0] = p / 1000;
  d[1] = (p % 1000) / 100;
  d[2] = (p % 100) / 10;
  d[3] = p % 10;
 // if (d[0] == d[1] || d[0] == d[2] || d[0] == d[3] || d[1] == d[2] || d[1] == d[3] || d[2] == d[3]) return 0;
  for (i = 0; i < 24; i++)  
  {
    int d1,d2,d3,d4;
    d1 = d[permus_of_four[i][0]];
    d2 = d[permus_of_four[i][1]];
    d3 = d[permus_of_four[i][2]];
    d4 = d[permus_of_four[i][3]];
    if(MASK_WITH_CHECK(FOUR_DIGIT(d1,d2,d3,d4),mask) && FOUR_DIGIT(d1,d2,d3,d4) > 1000 && FOUR_DIGIT(d1,d2,d3,d4) != p)
    {
      permus[num_pp] = FOUR_DIGIT(d1,d2,d3,d4);     
      num_pp++;
     // printf("%d is a prime permutation of %d\n",FOUR_DIGIT(d1,d2,d3,d4),p);
      //mask[CONV_TO_MASK(FOUR_DIGIT(d1,d2,d3,d4))] = 0;
    }
  }
  
  if (num_pp >= 2)
  {
    for (i = 0; i < num_pp; i++)
    {
      int j;
      for (j = 0; j < num_pp; j++)
      {
        if (permus[j] == p + 2*(permus[i] - p) || permus[j] == (p+permus[i])/2) return 3;
      }
    }
  }
  
  return 0;
}

