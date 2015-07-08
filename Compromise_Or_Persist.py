import numpy as np
from scipy.misc import comb
import math

def card_val(n,ncards, rank):
  '''
  n: number of cards in the game
  ncards: Total number of cards drawn, including the one in Alice's hand.
  rank: Number of cards previously seen greater than Alice's card.
  RETURN: Expected value of card
  '''
  #numerator
#  s = 0
  #denominator
 # d = 0
  #for i in xrange(ncards - rank,n - rank + 1):
   # c = comb(n - i,rank)*comb(i - 1,ncards - rank - 1)
    #s += i * c
    #d += c
  return (ncards-rank)*(n+1.)/(ncards+1.)

def expected_score(n):
  turn = n - 1
  e = (n+1) / 2.
  while turn:
    r_min = math.ceil(turn - (turn+1.)*e/(n+1.))
    s_new = ((n+1.) / (turn+1.))*(turn - r_min)*(turn - r_min + 1) / 2.
    e = (s_new + r_min*e)/turn
    turn = turn - 1
  return e


def expected_old(n,turn = 1):
  if turn == n:
    return (n+1)/2.
  s = 0.
  e = expected_old(n,turn+1)

  for rank in xrange(0,turn):
    c = card_val(n,turn,turn - rank - 1)
    if c < e:
      s += c

    else:
      return (s + (turn-rank)*e)/turn

    
print expected_score(1000000)
print expected_old(100)
