#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define MOD 1000000007
#define MAT_SIZE 200

typedef long long int LL;

int mod_matmul2D(int m, int n, int p, LL** a, LL** b, LL** c,LL mod)
{
   int i,j,k;
#pragma omp parallel shared(a,b,c) private(i,j,k) 
   {
#pragma omp for  schedule(static)
   for (i=0; i<m; i=i+1){
      for (j=0; j<n; j=j+1){
         a[i][j]=0.;
         for (k=0; k<p; k=k+1){
            a[i][j]=((a[i][j])+((b[i][k])*(c[k][j])))%mod;
         }
      }
   }
   }
   return 0;
}

int main()
{
    FILE *arr;
    LL k[MAT_SIZE][MAT_SIZE];
    arr =fopen("trans_mat.txt","r");
    int i,j;
     
     
    for(i=0 ;i<MAT_SIZE; i++)
    {
        for(j=0; j<MAT_SIZE; j++)
        {
            fscanf(arr, "%lld%*[^\n]%*c",&k[i][j]);
            printf("%lld\n", k[i][j]);
        }
    }
    
}
