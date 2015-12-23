#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <string.h>
#include <fstream>
#include <iostream>

#define MOD 1000000007LL
#define MAT_SIZE 2816

typedef unsigned long long int LL;
using namespace std;

void print_T(int mat[MAT_SIZE][MAT_SIZE]);
void print_vec(int * v, int size);
int res[MAT_SIZE][MAT_SIZE];
int T[MAT_SIZE][MAT_SIZE];
int temp_t[MAT_SIZE][MAT_SIZE]; // stores T transpose. should help multiply better

int mod_matmul2D(int a[MAT_SIZE][MAT_SIZE], int b[MAT_SIZE][MAT_SIZE],int c[MAT_SIZE][MAT_SIZE],LL mod)
{
   int i,j,k;
   
   for (i=0;i<MAT_SIZE;i++)
   {
     for (j=0;j<MAT_SIZE;j++)
     {
      temp_t[i][j] = c[j][i];
     }
   }
   
#pragma omp parallel shared(a,b,c) private(i,j,k) 
   {
#pragma omp for  schedule(static)
   for (i=0; i<MAT_SIZE; i=i+1){
      for (j=0; j<MAT_SIZE; j=j+1){
         a[i][j]=0;
         for (k=0; k<MAT_SIZE; k=k+1){
            a[i][j]=(a[i][j]+ ( (LL)(b[i][k]))* ( (LL)(temp_t[j][k]) ) )%mod;
         }
      }
   }
   }
   return 0;
}

void mod_mat_vec_mul(int mat[MAT_SIZE][MAT_SIZE],int * vec,int * res,LL mod)
{
 int i,j;
 register int tmp;
 register int sum;
 for (i=0;i<MAT_SIZE;i++)
 {
  sum = 0;
  for (j=0;j<MAT_SIZE;j++)
  {
   sum = (sum+(((LL)(vec[j]))*((LL)(mat[i][j])) ) ) %mod;
  }
  res[i] = sum;
 }
}

void mod_mat_exp(LL n,int mat[MAT_SIZE][MAT_SIZE],int* init)
{
 int* vec_res = (int*)malloc(MAT_SIZE*sizeof(int));
 while (n)
 {
   if (n&1)
   {
     mod_mat_vec_mul(mat,init,vec_res,MOD);
     memcpy(init,vec_res,MAT_SIZE*sizeof(int));
   }
   mod_matmul2D(res,mat,mat,MOD);
   memcpy(mat,res,MAT_SIZE*MAT_SIZE*sizeof(int));
   n/=2;
   printf("On n=%llu\n",n);
 }
 
}

void print_vec(int * v, int size)
{
  int i;
  printf("[");
  for (i = 0; i < size; i++)
  {
    printf("%d ",v[i]);
  }
  printf("]\n");
}

void print_mat(int * mat,int nrows, int ncols)
{
 int i,j;
 printf("\n");
 for (i=0;i<nrows;i++)
 {
  for (j=0;j<ncols;j++)
  {
   printf("%d ",mat[ncols*i+j]);
  }
  printf("\n");
 }
 printf("\n");
}

void print_T(int mat[MAT_SIZE][MAT_SIZE])
{
 int i,j;
 printf("\n");
 for (i=0;i<MAT_SIZE;i++)
 {
  for (j=0;j<MAT_SIZE;j++)
  {
   printf("%d ",mat[i][j]);
  }
  printf("\n");
 }
 printf("\n");

}

int main(int argc, char** argv)
{
  int i,j,tind;
  LL n = 1000000000000000000LL;
 // LL n = 2LL;
  
  if (argc < 3)
  {
   printf("Usage transition_matrix_file terminal_states file\n");
   exit(1);
  }
  
  fstream mat_file;
  fstream term_states_file;
  
  mat_file.open(argv[1]);
     
  for(i=0 ;i<MAT_SIZE; i++)
  {
    for(j=0; j<MAT_SIZE; j++)
    {
      mat_file >> T[i][j];
    }
  }
  
  mat_file.close();
//  printf("Completed reading mat file.\n");
  int* init = (int*)malloc(MAT_SIZE*sizeof(int));
  memset(init,0,MAT_SIZE*sizeof(int));
 // printf("Sucessfully allocated init vector, size %d\n",MAT_SIZE);
  init[0]=1;
  
  mod_mat_exp(n,T,init);

  print_vec(init,MAT_SIZE);
    
  LL sum=0;
  
  term_states_file.open(argv[2]);
  while (!term_states_file.eof())
  {
   term_states_file >> tind;
   if (0<=tind && tind < MAT_SIZE) sum = (sum + init[tind])%MOD;
  }
  printf("\nFinal Sum for n=%llu: %llu\n",n,sum);
  
}
