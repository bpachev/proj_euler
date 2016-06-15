from itertools import product

def pTilings(n):
    if n == 1:
        return 3

    first_up = n-1
    curr = {}
    for el in product(range(3), repeat = n-1):
        tot = 4
        for el1, el2 in zip(el[:-1], el[1:]):
            if el1 == el2:
                tot *= 2
        curr[el] = tot

    cands = {}
    opposites = {c : [other for other in range(3) if not other == c] for c in xrange(3)}
    for color_pair in product(range(3), repeat = 2):
        cands[color_pair] = [k for k in xrange(3) if k not in color_pair]

    for i in xrange(first_up):
        #do up step
        new = {}
        for el in curr:
            l = []
            for c in el:
                l.append(opposites[c])
#            print el, l
            for new_el in product(*l):
                if new_el not in new:
                    new[new_el] = curr[el]
                else:
                    new[new_el] += curr[el]
#        print new
        curr = new
        if i == first_up - 1:
            break
        new = {}
        #do narrowing step
        for el in curr:
            l = [cands[pair] for pair in zip(el[:-1], el[1:])]
            for new_el in product(*l):
                if new_el not in new:
                    new[new_el] = curr[el]
                else:
                    new[new_el] += curr[el]
        curr = new
    print 3*curr[(0,)]

pTilings(8)
