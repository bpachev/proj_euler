from fractions import gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        print b//a,b%a
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def solve(p,q):
 d = gcd(p,q)
 print d
 egcd(p/d,q/d)
solve(123456789,987654321)
