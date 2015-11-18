#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define CONV_TO_MASK(i) ((i-1)/2 - 1)
#define MASK_WITH_CHECK(i,mask) (((i)%2==0) ? 0 : mask[(i-1)/2 - 1])
#define P_UNDER_1000 169
#define P_UNDER_MILLION 78498
#define P_TEN_THOUSAND 1229
#define MAX_CACHE 80000000
#define SIX_DIGIT(d1,d2,d3,d4,d5,d6) (d1*100000+d2*10000+d3*1000+d4*100+d5*10+d6)
#define GET_SIX_DIGITS(d1,d2,d3,d4,d5,d6,num) d1 = num/100000;d2 = (num%100000)/10000;d3 = (num%10000)/1000;d4 = (num%1000)/100;d5 = (num%100)/10;d6 = num%10;

#define FIVE_DIGIT(d1,d2,d3,d4,d5) (d1*10000+d2*1000+d3*100+d4*10+d5)
#define GET_FIVE_DIGITS(d2,d3,d4,d5,d6,num) d2 = num/10000;d3 = (num%10000)/1000;d4 = (num%1000)/100;d5 = (num%100)/10;d6 = num%10;

#define FOUR_DIGIT(d1,d2,d3,d4) (d1*1000 + d2*100 + d3*10 + d4)
#define GET_FOUR_DIGITS(d1,d2,d3,d4,num)  d1 = num/1000;d2 = (num%1000)/100;d3 = (num%100)/10;d4 = num%10;
void prime_mask(char* mask, int c);
void big_prime_mask(char* mask, unsigned long long int c); 
void prime_mask_and_arr(char* mask, int c, int* primes, int nump);
void big_prime_mask_and_arr(char* mask, int c, long int* primes, int nump);
void really_big_prime_mask_and_arr(char* mask, unsigned long long int c, unsigned long long int* primes, unsigned long long int nump);
int slow_prime_check(long int n);
int faster_prime_check(long int n,int * primes, int nump);
int big_faster_prime_check(unsigned long long int n, unsigned long long int* primes, unsigned long long int nump);
void tot_fill(char * mask, int c, int * tot);

