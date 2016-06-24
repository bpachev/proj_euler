#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define VEC_SIZE 3
#define SWAP(a,b,t) t=a;a=b;b=t;

unsigned long long int min_lattice_vector(long long int * a, long long int * b);
unsigned long long int lin_comb_mag(long long int * a, long long int * b, long long int c, long long int d);
void lin_comb(long long int * dest, long long int * a, long long int * b, long long int c, long long int d);
unsigned long long int l1_norm(long long int * a);
long long int line_search(long long int * a, long long int * b,unsigned long long int a_norm);
void swap(long long int * a, long long int * b, int size);
void print_vec(long long int * v, int size);

void print_vec(long long int * v, int size)
{
  int i;
  printf("[");
  for (i = 0; i < size; i++)
  {
    printf("%lld ",v[i]);
  }
  printf("]\n");
}


void swap(long long int * a, long long int * b, int size)
{
  long long int temp = 0;
  for (int i = 0; i <= size; i++) {
    temp = a[i];
    a[i] = b[i];
    b[i] = temp;
  }
}

//negate a
void negate(long long int * a);

void negate(long long int * a)
{
  for (int i = 0; i < VEC_SIZE; i++) {
    a[i] = -a[i]; 
  }
}

int main()
{
  long long int * V, * W,* past_trib, * curr_trib,*tmp;
  unsigned long long int mod = 10000000;
  unsigned long long int num_blocks = 20000000;
  unsigned long long int checkpoint = 100000;
  unsigned long long int sum = 0;
  int block_size = 12;
  V = (long long int *)malloc(VEC_SIZE*sizeof(long long int));
  if (!V) {printf("Memory Error"); exit(1);}

  W = (long long int *)malloc(VEC_SIZE*sizeof(long long int));
  if (!W) {printf("Memory Error"); exit(1);}

  curr_trib = (long long int *)malloc(block_size*sizeof(long long int));
  if (!curr_trib) {printf("Memory Error"); exit(1);}

  past_trib = (long long int *)malloc(block_size*sizeof(long long int));
  if (!past_trib) {printf("Memory Error"); exit(1);}

  past_trib[block_size-1] = 0;
  past_trib[block_size-2] = 1;
  past_trib[block_size-3] = -1;

  for (int i = 0; i < num_blocks; i++)
  {
    curr_trib[0] = (past_trib[block_size-1] + past_trib[block_size-2] + past_trib[block_size-3]) % mod;
    curr_trib[1] = (curr_trib[0] + past_trib[block_size-1] + past_trib[block_size-2]) % mod;
    curr_trib[2] = (curr_trib[1] + curr_trib[0] + past_trib[block_size-1]) % mod;
    for (int j = 3; j < block_size; j++) {
      curr_trib[j] = (curr_trib[j-1] + curr_trib[j-2] + curr_trib[j-3] ) % mod;
    }
    V[0] = curr_trib[0] - curr_trib[1];
    V[1] = curr_trib[2] + curr_trib[3];
    V[2] = curr_trib[4]*curr_trib[5];
    W[0] = curr_trib[6] - curr_trib[7];
    W[1] = curr_trib[8] + curr_trib[9];
    W[2] = curr_trib[10]*curr_trib[11];
    sum += min_lattice_vector(W, V);
    if ((i + 1) % checkpoint == 0) {
      printf("On S(%d), current sum %llu\n",i+1,sum);
    }

    SWAP(curr_trib,past_trib,tmp)
  }
  printf("FINAL SUM: %llu\n",sum);
  

}

unsigned long long int min_lattice_vector(long long int * a, long long int * b)
{
  unsigned long long int a_norm, b_norm, temp, a_minus_b, a_plus_b;
  long long int k = 0;
  long long int * t;

  a_norm = l1_norm(a);
  b_norm = l1_norm(b);

  //ensure a has greater norm
  if (a_norm < b_norm) {
    SWAP(a_norm,b_norm,temp)
    SWAP(a,b,t)
  }
  
  a_minus_b = lin_comb_mag(a,b,1,-1); // = |a-b|
  a_plus_b = lin_comb_mag(a,b,1,1); // = |a+b|

  if (a_minus_b < b_norm) {
    lin_comb(b,a,b,1,-1); // b = a - b
    SWAP(a_minus_b,b_norm,temp)
  }

  if (a_minus_b >= a_norm)  {
    if (a_plus_b >= a_norm) // already reduced
    {
   //   printf("Already Reduced\n");
      return b_norm;
    }
    else if (a_plus_b < b_norm) {
      negate(a); // a = -a, swapping |a + b| and |a - b|
      SWAP(a_minus_b,a_plus_b,temp)
      lin_comb(b,a,b,1,-1); // b = a - b
      SWAP(a_minus_b,b_norm,temp)
  //    printf("NOT well-ordered, case 1\n");
    }
    else {
      negate(a); // a = -a, swapping |a + b| and |a - b|
      SWAP(a_minus_b,a_plus_b,temp)
//      printf("NOT well-ordered, case 2\n");
    }
  }

  while (a_norm > a_minus_b)
  {
    k = line_search(a,b,a_norm);
    lin_comb(a,a,b,1,k); // a = a + k*b
    a_minus_b = lin_comb_mag(a,b,1,-1); // = |a-b|
    a_plus_b = lin_comb_mag(a,b,1,1); // = |a+b|
    if (a_plus_b < a_minus_b) 
    {
      negate(a);
      SWAP(a_plus_b, a_minus_b,temp)
    }

    a_norm = l1_norm(a); 
    if (b_norm > a_norm)
    {
      SWAP(a,b,t)
      SWAP(a_norm,b_norm,temp)
    }

  }

  unsigned long long int max_norm, min_norm;

  b_norm = l1_norm(b);
  
  if (a_norm > b_norm)
  {
    max_norm = a_norm;
    min_norm = b_norm;
  }

  else
  {
    max_norm = b_norm;
    min_norm = a_norm;
  }  

  if (a_minus_b < max_norm || a_plus_b < max_norm) {
    printf("ERROR. Conditions of theorem not satisfied. Results inaccurate.\n");
    printf("|a-b| = %llu, |a+b| = %llu, |a| = %llu, |b| = %llu\n",a_minus_b, a_plus_b,a_norm,b_norm);
    print_vec(a,VEC_SIZE);
    print_vec(b,VEC_SIZE); 
  }

  return min_norm;
}


unsigned long long int lin_comb_mag(long long int * a, long long int * b, long long int c, long long int d)
{
  unsigned long long int res = 0;
  for (int i = 0; i < VEC_SIZE; i++) {
    long long int temp = c*a[i] + d*b[i];
    if (temp > 0) res += (temp);
    else res += -temp; 
  }
  return res;  
}

void lin_comb(long long int * dest, long long int * a, long long int * b, long long int c, long long int d)
{
  for (int i = 0; i < VEC_SIZE; i++) {
    dest[i] = c*a[i] + d*b[i];
  }
}


unsigned long long int l1_norm(long long int * a)
{
  unsigned long long int res = 0;
  for (int i = 0; i < VEC_SIZE; i++) {
    if (a[i] > 0) res += a[i];
    else res += -a[i]; 
  }
  return res;
}

long long int line_search(long long int * a, long long int * b,unsigned long long int a_norm)
{
  long long int k_min = 0;
  unsigned long long int min = a_norm;
  unsigned long long int temp = 0;
  long long int k_temp = 0;
  for (int i = 0; i < VEC_SIZE; i++)  {
    if (b[i]) {
      k_temp = -a[i]/b[i];
      temp = lin_comb_mag(a,b,1,k_temp);
      if (temp < a_norm) {
        min = temp;
        k_min = k_temp;
      }
      
      k_temp = -a[i]/b[i] - 1;
      temp = lin_comb_mag(a,b,1,k_temp);
      if (temp < a_norm) {
        min = temp;
        k_min = k_temp;
      }
    }
  }
  return k_min;
}



