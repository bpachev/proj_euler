letters = ['F','E','A','R']
words = ["FREE","FARE","AREA","REEF"]
word_dict = {w:i for i,w in enumerate(words)}

def do_trans(state, letter):
	word = "".join(state[:3])+letter
	if word in word_dict:
		ind = word_dict[word]
		if state[3+ind]:
			return None
		mask = list(state[3:])
		mask[ind] = True
		new_state = tuple(word[-3:]) + tuple(mask)
		return new_state
	else:
		return tuple(word[-3:]) + state[3:]
from itertools import product

def build_states():
	states = []
	for last_three in product(letters,repeat=3):
		for mask in product([False, True], repeat=4):
			states.append((last_three+mask))
	rev_dict = {state: i for i, state in enumerate(states)}
	print len(states)
	transitions = {i:[] for i in range(len(states))}
	for i, state in enumerate(states):
		for l in letters:
			new_state = do_trans(state, l)
			if new_state is not None:
				transitions[i].append(rev_dict[new_state])
	return states, transitions, rev_dict

def solve(n):
	states, trans, rev_dict = build_states()
	vec = [0]*len(states)
	terminal_states = []
	for last_three in product(letters, repeat=3):
		ind = rev_dict[last_three + tuple([False]*4)]
		vec[ind] = 1
		term_ind = rev_dict[last_three + tuple([True]*4)]
		terminal_states.append(term_ind)
	for it in range(n-3):
		new_vec = [0]*len(states)
		for i in range(len(states)):
			for j in trans[i]:
				new_vec[j] += vec[i]
		vec = new_vec
	print sum(vec[i] for i in terminal_states)
solve(30)
