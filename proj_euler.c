#include "proj_euler.h"

unsigned long long int mod_pow(unsigned long long int base, unsigned long long int exp, unsigned long long int mod)
{
    unsigned long long int result = 1;
    while (exp)
    {
        if (exp % 2)
        {
          result = (result * base) % mod;
        }
        exp = exp / 2;
        base = (base * base) % mod;
    }

    return result;
}

//signed mod pow
LL smod_pow(LL base, LL exp, LL mod)
{
    LL result = 1;
    while (exp)
    {
        if (exp % 2)
        {
          result = (result * base) % mod;
        }
        exp = exp / 2;
        base = (base * base) % mod;
    }

    return result;
}

long long int isqrt(long long int n)
{
    long long int x = n;
    long long int y = (x + 1) / 2;
    while (y < x)
    {
        x = y;
        y = (x + n / x) / 2;
    }
    return x;
}

//with an inital guess
LL isqrt_init(LL n, LL init)
{
//  printf("isqrt_init(%lld, %lld)\n  ", n, init);
  if (init <= 0) init = 1;
  if (n == 0) return 0;
  LL x, y;

  if (init < n / init) init = n/init;
    x = init + 1;
    y = init;
    while (y < x)
    {
        x = y;
        y = (x + (n / x) ) / 2;
    }

/*  else
  {
    x = init - 1;
    y = init;
    while (y > x)
    {
        if (n == 4224) printf("%lld, %lld\n", x, y);
        x = y;
        y = (x + (n / x)) / 2;
    }

  }*/

  return x;
}

LL modinv(LL n, LL mod)
{
  LL s,t;
  LL d = EEA(n,mod,&s,&t);
  if (d != 1) printf("WARNING: %lld and %lld are not coprime, and the modular inverse does not exist.\n",n,mod);
  return s % mod;
}

LL EEA(LL a, LL b,LL * s_res,LL * t_res)
{
  /*
  RETURNS r, s, t
  r -- gcd(a,b)
  s and t satisfy as + bt = d
  */
  LL an,bn,s_prev,t_prev,s,t,r_curr,r_next,r_old, t_old, s_old,q;
  an = a;
  bn = b;
  if (b > a)
  {
    bn = a;
    an = b;
  }

  s_prev = 1;
  t_prev = 0;
  s = 0;
  t = 1;
  r_curr = an;
  r_next = bn;
  while (r_next)
  {
    r_old = r_next;
    t_old = t;
    s_old = s;
    q = r_curr/r_next;
    r_next = r_curr%r_next;
    r_curr = r_old;
    t = t_prev - q*t;
    s = s_prev - q*s;
    s_prev = s_old;
    t_prev = t_old;
  }

  if (a > b)
  {
    (*s_res) = s_prev;
    (*t_res) = t_prev;
  }
  else
  {
    (*s_res) = t_prev;
    (*t_res) = s_prev;
  }

  return r_curr;
}



LL big_gcd(LL a, LL b)
{
  if (b == 0) return a;
  else return big_gcd(b,a%b);
}


int gcd(int a, int b)
{
  if (b == 0) return a;
  else return gcd(b,a%b);
}




LL big_bin_search(LL*a,LL l, LL u,LL n)
{
  if (n < a[l])
  {
    return l+1;
  }

  else if (n > a[u])
  {
    return u+1;
  }

  else if (n == a[u]) return u+1;
  else if (n == a[l]) return l+1;
  else
  {
    if (u == l+1) return l + 1;
    LL mid = (u+l)/2;
    if (n == a[mid]) return mid + 1;
    if (n > a[mid]) return big_bin_search(a,mid,u,n);
    else return big_bin_search(a,l,mid,n);
  }
}

int bin_search(int*a,int l, int u,int n)
{
  if (n < a[l])
  {
    return l+1;
  }

  else if (n > a[u])
  {
    return u+1;
  }

  else if (n == a[u]) return u+1;
  else if (n == a[l]) return l+1;
  else
  {
    if (u == l+1) return l + 1;
    int mid = (u+l)/2;
    if (n == a[mid]) return mid + 1;
    if (n > a[mid]) return bin_search(a,mid,u,n);
    else return bin_search(a,l,mid,n);
  }
}


int digit_root(int n)
{
  if (n < 10) return n;
  else return digit_root(digit_sum(n,10));
}

int digit_sum(int n, int base)
{
  int s = 0;
  while (n)
  {
    s += n % base;
    n /= base;
  }
  return s;
}

LL big_digit_root(LL n)
{
  if (n < 10) return n;
  else return big_digit_root(big_digit_sum(n,10LL));
}


LL big_digit_sum(LL n, LL base)
{
  LL s = 0;
  while (n)
  {
    s += n % base;
    n /= base;
  }
  return s;
}

void print_big_vec(LL * v, LL size)
{
  LL i;
  printf("[");
  for (i = 0; i < size; i++)
  {
    printf("%lld ",v[i]);
  }
  printf("]\n");
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

LL * big_arr(LL size, LL init)
{
  LL s = size*sizeof(LL);
  LL* arr = (LL*)malloc(s);
  if (!arr)
  {
    die("Error allocating array of size %lld long longs to initial value of %lld.\n",size,init);
  }

  for (int i = 0; i < size; i++) arr[i] = init;
  return arr;
}

//the order of a prime in a factorial
LL pfact_ord(LL n,LL p)
{
 LL res = 0;
 while (n)
 {
  n/=p;
  res += n;
 }
 return res;
}

//exponent of a prime p in the factorization of n
//Or the highest power of p dividing n, in general
LL p_ord(LL n, LL p)
{
 LL res = 0;
 if (!n) return 0;
 while (n%p)
 {
  res++;
  n  /= p;
 }
 return res;
}

void die(const char* msg, ...)
{
  va_list ap;
  va_start(ap,msg);

  fprintf(stderr, "fatal_error: ");
  vfprintf(stderr, msg, ap);
  va_end(ap);
  fputc('\n',stderr);
  exit(1);
}
