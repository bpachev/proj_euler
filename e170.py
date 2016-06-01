import itertools as it

def isPandigital(n):
    mask = [0]*10
    while n:
        i = n%10
        if mask[i]: return False
        mask[i] = 1
        n /= 10
    return True

def tnum(s):
    r = 0
    for el in s:
        r *= 10
        r += el
    return r

ten_pows = [10**i for i in xrange(13)]

def check_two_digits():
    res = []
    digits = set(range(10))
    for i in xrange(12, 100):
        q, r = divmod(i,10)
        if r and i % 11:
            other = list(digits - set((q,r)))
            for p in it.permutations(other):
                if not p[0]: continue
                t = p[0]
                for j in xrange(1,8):
                    m1 = i*t
                    t *= 10
                    t += p[j]
                    if not p[j]: continue
                    if m1 >= ten_pows[j+1]: continue
                    m2 = i*tnum(p[j:])
                    if m2 >= ten_pows[8-j+1]: continue
                    if isPandigital(m1 + m2* ten_pows[j+1]):
                        res.append(max(m1 + m2* ten_pows[j+1], m2 + m1* ten_pows[9-j]))
    print max(res)

check_two_digits()
