def digit_sum(n,base=10):
  tot = 0
  while n:
    tot += n%10
    n /= 10
  return tot

def gen_digit_seq(n):
    start = 1
    for i in xrange(n-1):
        print digit_sum(start), start
        start += digit_sum(start)

gen_digit_seq(5000)
