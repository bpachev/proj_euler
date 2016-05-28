
def Q(m, n):
    res = 0
    #count contributions from (n+1)^m
    temp = n+1
    while temp:
        temp /= 2
        res += m * temp

    #now count contributions from ((n+2)/2)^m - 1
    #if n is odd, then -m happens
    res -= (n-n/2) * m
    temp = n/2
    l = 0
    while temp:
        temp /= 2
        res += temp
    return res

m = 904961
print Q(m, 10**12)
