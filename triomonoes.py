import numpy as np
from itertools import product

pieces = []
#left-up corner
pieces.append([0b01,0b11,0])
#left-down corner
pieces.append([0b10,0b11,0])
#right-up corner
pieces.append([0b11,0b01,0])
#right-down corner
pieces.append([0b11,0b10,0])
#three vertical
pieces.append([0b111,0,0])
#three horizontal
pieces.append([0b01,0b01,0b01])

def shifted_pieces(pieces, shift, mask):
    res = []
    shift = 2**shift
    for p in pieces:
        new_p = []
        too_big = False
        for el in p:
            new_el = el * shift
            if new_el > mask:
                too_big = True
                break

            new_p.append(new_el)

        if too_big: continue
        res.append(new_p)
    return res

def print_state(side_len, state):
    for el in state:
        m = 1
        out = ""
        for i in xrange(side_len):
            out += str(1&(el/m)) + " "
            m *= 2
        print out

def gen_transitions(pieces, side_len):
    mask = 2**side_len-1
    res = [[0,0,0]]
    pieces = shifted_pieces(pieces, 0, mask)
    for i in xrange(side_len):
        temp = []
        for prev in res:
            for piece in pieces:
                #detect overlap
#                print [p&s for p,s in zip(piece, prev)]
#                print p, prev
                new = [p|s for p,s in zip(piece, prev)]
#                print new, piece, prev
                if sum([p&s for p,s in zip(piece, prev)]):
                    continue
                else:
                    temp.append(new)
        res += temp
        pieces = shifted_pieces(pieces, 1, mask)
    return res


#print len(set([tuple(a) for a in gen_transitions(pieces, 9)]))

def indexed_transitions(side_len):
    global pieces
    trans = gen_transitions(pieces, side_len)
    res = {i: [] for i in xrange(2**side_len)}
    for el in trans:
        res[el[0]].append(el)
    return res

#print indexed_transitions(3)

def gen_states(side_len):
    base = range(3)
    #twos mean that a three horizontal is 'sticking out', and the corresponding bit is set in both places
    states = []
    for comb in product(base, repeat = side_len):
        s = [0,0]
        for el in comb:
            b1, b2 = 0,0
            if el >= 1:
                b1 = 1
            if el == 2:
                b2 = 1
            s[0] *= 2
            s[0] += b1
            s[1] *= 2
            s[1] += b2
        states.append(s)
#        print comb, s
#        print_state(side_len,s)

    return states

gen_states(2)

def solve(n, k):
    if (n*k) % 3 > 0:
        return 0

    side_len = min(n,k)
    ntransitions = max(n,k)
    mask = 2**side_len - 1

    states = [tuple(s) for s in gen_states(side_len)]
    trans = indexed_transitions(side_len)
    tdict = {s:[] for s in states}

    for s in states:
        for t in trans[mask^s[0]]:
            assert t[0]|s[0] == mask and t[0]&s[0] == 0
            if t[1]&s[1]: continue

            new_s = (t[1]|s[1], t[2])
            tdict[s].append(new_s)

#    print tdict
    scounts = {s:0 for s in states}
    scounts[(0,0)] = 1
    for i in xrange(ntransitions):
        new_scounts = {s:0 for s in states}
        for s in scounts:
            num_reps = scounts[s]
            if not num_reps:
                continue
            for s2 in tdict[s]:
                new_scounts[s2] += num_reps
        scounts = new_scounts
#    print scounts
    return scounts[(0,0)]

print solve(9,12)
