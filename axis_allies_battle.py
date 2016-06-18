import numpy as np
import numpy.linalg as la
from collections import Counter
from scipy.stats import binom
from itertools import product

class unit:
    def __init__(self, attack, defense, cost, name):
        self.attack = attack
        self.defense = defense
        self.cost = cost
        self.name = name

TANK = unit(3,3,5,"Tank")
INF = unit(1,2,3,"Infantry")
ART = unit(2,2,4,"Artillery")
FIGHT = unit(3,4,10, "Fighter")
BOMB = unit(4,1,12, "Bomber")

def attack_dist(unit_list):
    narts = 0
    for unit in unit_list:
        if unit.name == ART.name:
            narts += 1

    first = unit_list[0]
    dist_list = [np.array([1-first.attack/6., first.attack/6.])]
    for unit in unit_list[1:]:
        old = dist_list[-1]
        new = [0] * (len(old) + 1)
        if unit.name == INF.name and narts > 0:
            p = 2/6.
            narts -= 1
        else:
            p = unit.attack / 6.
        new[-1] = p * old[-1]
        new[0] = (1-p) * old[0]
        for i in xrange(1,len(old)):
            new[i] = p * old[i-1] + (1-p) * old[i]
        dist_list.append(np.array(new))
    return dist_list

def defense_dist(unit_list):
    first = unit_list[0]
    dist_list = [np.array([1-first.defense/6., first.defense/6.])]
    for unit in unit_list[1:]:
        old = dist_list[-1]
        new = [0] * (len(old) + 1)
        p = unit.defense / 6.
        new[-1] = p * old[-1]
        new[0] = (1-p) * old[0]
        for i in xrange(1,len(old)):
            new[i] = p * old[i-1] + (1-p) * old[i]
        dist_list.append(np.array(new))
    return dist_list

def battle_odds(attackers, defenders):
    attackers = sorted(attackers, key = lambda unit: -unit.cost)
    defenders = sorted(defenders, key = lambda unit: unit.cost)
    adist = attack_dist(attackers)
    ddist = defense_dist(defenders)
    na = len(attackers)
    nd = len(defenders)
    states = list(product(range(na+1), range(nd+1)))
    states_to_inds = {state : i for i, state in enumerate(states)}
    T = np.zeros((len(states), len(states)), dtype = np.float64)
    for state in states:
        nattack, ndefend = state
        i = states_to_inds[state]
        if nattack == 0 or ndefend == 0:
            T[i,i] = 1
        else:
            for ahits in xrange(nattack + 1):
                new_defend = max(ndefend - ahits, 0)
                for dhits in xrange(ndefend + 1):
                    new_attack = max(nattack - dhits, 0)
                    new_state = (new_attack, new_defend)
                    j = states_to_inds[new_state]
                    T[j,i] += adist[nattack-1][ahits] * ddist[ndefend-1][dhits]
    init = np.zeros(T.shape[0])
    init[-1] = 1
    evals, evecs = la.eig(T)
    for i in xrange(20):
        init = T.dot(init)
#    print init
    print "Draw", init[0]
    attack_odds = np.array([init[states_to_inds[(nattackers, 0)]] for nattackers in xrange(1,na+1)])
    defend_odds = np.array([init[states_to_inds[(0, ndefenders)]] for ndefenders in xrange(1, nd+1)])
    acosts = np.array([unit.cost for unit in attackers])
    dcosts = np.array([unit.cost for unit in defenders])
    print "Attackers win", np.sum(attack_odds)
    print attack_odds
    print "Expected losses", np.sum(acosts) - attack_odds.dot(np.cumsum(acosts))
    print "Defenders win", np.sum(defend_odds)
    print defend_odds
    print "Expected losses", np.sum(dcosts) - defend_odds.dot(np.cumsum(dcosts))


attacking =  [ART]+[INF]+[BOMB]
defending = 2*[INF]
battle_odds(attacking, defending)
