#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdarg.h"

typedef long long int LL;
typedef unsigned long long int ULL;


unsigned long long int mod_pow(unsigned long long int base, unsigned long long int exp, unsigned long long int mod);
LL smod_pow(LL base, LL exp, LL mod);
long long int isqrt(long long int n);
LL isqrt_init(LL n, LL init);

int digit_sum(int n, int base);
LL big_digit_sum(LL n, LL base);
LL big_bin_search(LL*a,LL l, LL u,LL n);
int bin_search(int*a,int l, int u,int n);
void print_big_vec(LL * v, LL size);
void print_vec(int * v, int size);
int gcd(int a, int b);
LL big_gcd(LL a, LL b);
LL EEA(LL a, LL b,LL * s_res,LL * t_res);
LL modinv(LL n,LL mod);
LL big_digit_root(LL n);
int digit_root(int n);
LL * big_arr(LL size, LL init);
LL pfact_ord(LL n, LL p);
LL p_ord(LL n, LL p);
void die(const char* msg, ...);
