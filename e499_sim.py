import random

def sim_game():
  '''
  Returns winnings, the amount won
  '''
  
  pot = 1
  while True:
    if random.random() > .5:
      #heads
      pot *= 2
    else:
      #tails
      return pot


def sample_avg(num_games = 10.**3):
  total = 0    
  for i in xrange(num_games):
    total += sim_game()
  print "Average Winnings: " + str(total/float(num_games))


def sim_lottery(fortune,cost,maxgames = 500,thresh = 10**12):
  ngames = 0
  while fortune >= cost and ngames < maxgames:
    fortune += sim_game() - cost
#    print fortune
    ngames += 1
    if fortune > thresh:
      return 1
  if fortune < cost:
    return 0 #ran out of money 
  else:
#    print fortune
    return 1 #didn't run out


def avg_lottery(f,c,nl,mgames = 500,thresh = 10**12):
  nwins = 0
  for x in xrange(nl):
    nwins += sim_lottery(f,c,mgames,thresh) 
  print "Wins: " + str(nwins) + " Losses: " + str(nl - nwins)
  print "Won on average " + str(float(nwins)/nl)

avg_lottery(5,2,100000,500,1000)  