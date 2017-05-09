def solve(cap):
    #Define P(n,k) to be probability of p2 victory given it is her turn, p1 score n, p2 score k
    cache = {}
    def P(n,k):
        if n >= cap and k < cap:
            return 0
        elif k >= cap and n < cap:
            return 1
        else:
            return cache[(n,k)]

    for n in xrange(cap-1, -1, -1):
        for k in xrange(cap-1, -1, -1):
            #Find the optimal T
            max_prob = -1
            T = 1
            while True:
                #Determine the probability of victory assuming T is the optimal number of flips
                score = 2**(T-1)
                success_prob = 2.**(-T)
                #Determine self-loop probability. This is probability of p2 fail times p1 fail
                loop = .5 * (1. - success_prob)
                #Determine the probabilty of a non-loop and victory
                #Either p2 fails and p1 succeeds, so 
                s = (1-success_prob) * .5 * P(n+1, k)
                #Then success means victory
                if k + score >= cap:
                    s += success_prob
                else:
                    s += success_prob * (.5 * P(n+1, k+score) + .5 * P(n, k + score))
                # since prob = loop*prob + s
                prob = s/(1.-loop)
#                print s, prob, loop
                max_prob = max(max_prob, prob)
                if k + score >= cap: break
                T += 1
            
            cache[(n,k)] = max_prob
    print "{:.8f}" .format( .5*cache[(0,0)] + .5 * P(1,0))

solve(100)
