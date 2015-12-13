#include "proj_euler.h"

#define N 1000LL
#define A 1000000000LL
#define B 1000LL

//Computes a(n), where a(n+1) = 6*a(n)^2+10*a(n) + 3, and a(1) = 1
//Note that 6*a(n+1)+5 = 36*a(n)^2+60*a(n)+23 = (6*a(n)+5)^2 - 2 
//Letting T(n) = 6*a(n)+5, T(n+1) = T(n)^2 - 2, which has a closed form of
// x^(2^n) + y^(2^n) where x and y are the roots of x^2 - a*x + 1, and a = T(0)
// So we need here to shift indices. a(n) is really n-1 applications of the map.
//We assume that mod is prime
LL a(LL n,LL mod)
{
 LL exp = smod_pow(2LL,n-1,mod*mod-1);
 LL a1,a2,b1,b2;
 while (exp)
 {
   if (exp & 1LL)
   {
     //do mul
   }
   
 }
 return ((a1+b1 - 5LL) * smod_pow(6LL,mod-2,mod)) % mod; 
}

int main()
{
  
}
