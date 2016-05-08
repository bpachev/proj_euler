def digit_sum(n,base=10):
  tot = 0
  while n:
    tot += n%10
    n /= 10
  return tot

def gen_digit_seq(n):
    start = 1
    for i in xrange(n):
        start += digit_sum(start)
    return start


def first_cache():
    bound = 200
    cache = {}
    for prefix_sum in xrange(bound):
        for start_remainder in xrange(227):
            if start_remainder+prefix_sum == 0:
                continue
            steps = 0
            rem = start_remainder
            while rem < 1000:
                steps += 1
                rem += prefix_sum + digit_sum(rem)
            cache[(prefix_sum, start_remainder)] = (steps, rem%1000)
    return cache

def next_cache(prev, bound=200):
    cache = {}
    for prefix_sum in xrange(bound):
        for start_remainder in xrange(227):
            if start_remainder+prefix_sum == 0:
                continue
            steps = 0
            rem = start_remainder

            for i in xrange(100):
                try:
                    new_steps, rem = prev[(prefix_sum+digit_sum(i), rem)]
                except KeyError:
                    print start_remainder, prefix_sum, rem, i
                    return
                steps += new_steps
            cache[(prefix_sum, start_remainder)] = (steps, rem)
    return cache


def solve(n):
    caches = []
    caches.append(first_cache())
    for i in xrange(7):
        caches.append(next_cache(caches[-1], bound = 200-(i+1)*18))
    #print gen_digit_seq(n)
    level = len(caches)-1
    rem = 1
    pref = 0
    steps_left = n
    while True:
        if level < 0:
            while steps_left:
                pref += digit_sum(pref)
                steps_left -= 1
            return pref

        dec, new_rem = caches[level][(digit_sum(pref), rem)]
        if dec > steps_left:
            if level:
                pref *= 100
            else:
                pref = 1000*pref + rem
            level -= 1
            continue
        steps_left -= dec
        pref += 1
        rem = new_rem


    print caches[-1][(0, 1)]

if __name__ == "__main__":
    print solve(10**15-1)
