#include "proj_euler.h"

#define UPPER 20000000
#define LOWER 10000000
//#define UPPER 100
//#define LOWER 50

LL digit_intersects[10][10];


LL clock_diff(LL n)
{
  LL d = 0;
  //extract digits of i
  LL t =n;
  LL curr_num = 0;
  LL temp_digits[10];
  LL k = 0;
  memset(temp_digits,0,10*sizeof(LL));
  while (t)
  {
    temp_digits[k] = t % 10;
    t /= 10;
    k++;
  }
 // printf("Starting num: %lld\n",n);
  // The savings of Max's clock over Sam's occur when LLersection occurs. 
  while (1)
  {
    LL l;
    curr_num = 0;
    for (l=0;l<k;l++) curr_num += temp_digits[l];
    t = curr_num;
   // printf("Next Num:%lld\n",curr_num);
    k = 0;
    while (t)
    {
      d += 2*digit_intersects[t%10][temp_digits[k]]; //Sam's clock turns each segment off and then on, so 2*segments.
      temp_digits[k] = t%10;
      t /= 10;
      k++;
    }
 //   printf("Running Savings: %lld\n",d);
    if (curr_num < 10) break; 
  } 
  return d;
}

LL main()
{
  LL digit_mask[10];
  LL digit_segs[10];
  //bit-mask representation of the digital representations of the digits 0-9.
  //There are 7 possible segments. The middle horizontal one corresponds to the most significant bit.
  //The others proceed in counter-clockwise fashion. For example, 0 has all segments but the middle one.
  //5 has the middle, the top, the upper left, not the bottom left, the bottom, the bottom right, and not the top right.
  digit_mask[0] = 63;  //00111111
  digit_mask[1] = 3;   //00000011
  digit_mask[2] = 109; //01101101 
  digit_mask[3] = 103; //01100111
  digit_mask[4] = 83;  //01010011
  digit_mask[5] = 118; //01110110
  digit_mask[6] = 126; //01111110
  digit_mask[7] = 51;   //00110011
  digit_mask[8] = 127; //01111111
  digit_mask[9] = 119; //01110111

  LL i,j,k;
  for (i = 0; i < 10; i++)
  {
    digit_segs[i] = digit_sum(digit_mask[i], 2);
  }
  
  for (i = 0; i < 10; i++)
  {
    for (j = 0; j < 10; j++)
    {
      digit_intersects[i][j] = digit_sum(digit_mask[i] & digit_mask[j],2);
     // printf("intersection of %lld and %lld: %lld\n",i,j,digit_intersects[i][j]);
    }   
  }
  //clock_diff(19999999);
  char* mask = (char *)malloc(UPPER);
  memset(mask,1,UPPER);
  
  LL diff = 0;
  
  for (i = 2; i < UPPER; i++)
  {
    if (mask[i])
    {
      for (j = i + i; j < UPPER; j += i)
      {
        mask[j] = 0;
      }
      
      if (i > LOWER)
      {
      //  printf("p:%lld\n",i);
        diff += clock_diff(i);
      }
    }
  }
  printf("Total Difference: %lld\n",diff);
}

