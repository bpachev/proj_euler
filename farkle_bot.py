from itertools import product
import numpy as np
import json

def score_roll(roll):
    counts = np.zeros(7, dtype=int)
    for dice in roll:
        counts[dice] += 1

    # If we have 3 pairs or a straight - assume the player is smart enough to take the full points
    if np.sum(counts==2) == 3 or np.sum(counts==1) == 6:
        score = 1500
        dice_used = 6
        return [(score, dice_used)]

    # A list of all the distinct scoring options
    options = []

    # Check for a triples and higher
    # Naturally, if there are two triples there is no reason to not take both.
    score = 0
    dice_used = 0
    for i in range(1,7):
        if counts[i] >= 3:
            prefactor = i if i > 1 else 10
            score += prefactor * 100 * 2 ** (int(counts[i])-3)
            dice_used += int(counts[i])

    if score:
        options.append((score, dice_used))

    # assume that 1's are always taken before fives
    single_dice_score = 0
    single_dice_used = 0
    if counts[1] <= 2:
        for i in range(1, counts[1]+1):
            single_dice_score += 100
            single_dice_used += 1
            options.append((single_dice_score, single_dice_used))
    if counts[5] <= 2:
        for i in range(1, counts[5]+1):
            single_dice_score += 50
            single_dice_used += 1
            options.append((single_dice_score, single_dice_used))

    # we had a triple
    if single_dice_used < len(options):
        score, dice_used = options[0]
        for s, d in options[1:single_dice_used+1]:
            options.append((score+s, dice_used+d))
    return options

class Policy:
    """Represents a single policy
    """

    def __init__(self, utilities, distributions, objective_func=None, stop_utility=None):
        self.utilities = utilities
        self.distributions = distributions
        if objective_func is not None:
            self.stop_utility = {score: objective_func({score: 1}) for score in range(0, 10**4, 50)}
        elif stop_utility is not None:
            self.stop_utility = stop_utility
        else:
            raise ValueError("No way to determine stopping utility!")

    def should_stop(self, score, dice):
        return self.stop_utility[score] >= self.utilities[(score, dice)]

    def best_choice(self, score, dice, choices):
        util = -np.inf
        choice = None
        for points, dice_used in choices:
            k = (score+points, dice-dice_used if dice > dice_used else 6)
            if self.utilities[k] > util:
                choice, util = (points, dice_used), self.utilities[k]

        return choice

    def choice_from_roll(self, score, roll):
        options = score_roll(roll)
        return self.best_choice(score, len(roll), options)

    def to_json(self):
        """Convert data into a JSON-serializable format
        """

        return {"utilities": list(self.utilities.items()), "distributions": list(self.distributions.items()),
            "stop_utility": self.stop_utility}

    def simulateTurn(self):
        score, dice = 0, 6
        while not self.should_stop(score, dice):
            roll = np.random.randint(1, 7, size=dice)
            choice = self.choice_from_roll(score, roll)
            # FARKLE!
            if choice is None:
                return 0
            score += choice[0]
            dice -= choice[1]
            if not dice: dice = 6
        return score

    @staticmethod
    def from_json(data):
        for key in ["utilities", "distributions"]:
            data[key] = {tuple(k): v for k, v in data[key]}
        data["stop_utility"] = {int(k): v for k, v in data["stop_utility"].items()}
        return Policy(**data)

class FarkleBot:
    """Because I can't beat my brother-in-law with luck, I'm going to do it with MATH.

    This class is what we call serious overkill for a silly game.
    It has tools for computing optimal play strategies for different objectives.
    The goal is to DOMINATE at Farkle (at least assuming fair dice ;-)).
    """

    # Assume that after getting 10K in a turn, people will always stop
    MAX_TURN_SCORE = 10000


    def __init__(self, policyFile=None,
            transitions="farkle_summarized_transitions.json"):
        """Initializes the FarkleBot
        
        Args:
            policyFile - (str) A filename where cached policies are stored
                If None, policies will need to be computed
            transitions - (str) A JSON file where Cached Farkle transitions are stored
        """

        with open(transitions, "r") as fp:
            data = json.load(fp)
            self.transitions = {int(i): v for i,v in data.items()}
            self.transitions[1] = [[[[100, 1]], 1], [[[50, 1]],1], [[[0, 1]], 1], [[], 3]]

        if policyFile is None:
            self.policies = self.computeDefaultPolicies()
        else:
            with open(policyFile, "r") as fp:
                data = json.load(fp)
                self.policies = {name: Policy.from_json(v) for name, v in data.items()}

    def computeDefaultPolicies(self):
        policies = {}
        # compute take-500
        func = lambda x: sum(p if s >=500 else 0 for s, p in x.items())
        # Compute policy to get to 500 points in the best way possible
        policies["take_500"] = self.computePolicy(func)
        policies["max_score"] = self.computePolicy(lambda x: sum(s*p for s,p in x.items()))
        return policies

    def computePolicy(self, objective_func):
        """Compute a custom policy

        Args:
            objective_func - the utility function to maximize
                The function must accept a dictionary probs, which maps each possible score
                to the probability of getting that score. It should return a real number
                representing the utility of the score distribution.

        Returns:
            utilities - a dictionary mapping states to utility to use in decision-making
            distributions - a dictionary mapping states to full score distributions
        """

        scores = range(0, self.MAX_TURN_SCORE, 50)
        dice_remaining = range(1,7)
        states = list(product(scores[::-1], dice_remaining[::-1]))

        utilities = {}
        distributions = {}

        unsolved_states = states
        while len(unsolved_states) > 0:
            next_states = []
            for score, dice in unsolved_states:
                transitions = self.transitions[dice]

                if dice > 1 and score < self.MAX_TURN_SCORE-50 and (score+50, dice-1) not in utilities:
                    next_states.append((score, dice))
                    continue

                dist = {}
                for choices, repeats in transitions:
                    all_solved = True

                    # if there are no choices, we farkled
                    best_dist = {0:1}
                    best_util = -np.inf

                    for points, dice_used in choices:
                        new_score, new_dice = score+points, (dice-dice_used if dice > dice_used else 6)
                        if new_score >= self.MAX_TURN_SCORE:
                            best_dist = {new_score: 1}
                            best_util = objective_func(best_dist)
                            break
                        # account for the probability we stop next turn
                        else:
                            cand = {new_score:1}
                            util = objective_func(cand)
                            if util > best_util:
                                best_util, best_dist = util, cand

                        k = (new_score, new_dice)
                        if k not in utilities:
                            all_solved = False
                            break
                        elif utilities[k] > best_util:
                            best_util, best_dist = utilities[k], distributions[k]

                    if not all_solved:
                        next_states.append((score, dice))
                        break
                    else:
                        for s in best_dist:
                            dist[s] = dist.get(s,0) + repeats/6.**dice * best_dist[s]

                if all_solved:
                    #print(dist)
                    utilities[(score, dice)] = objective_func(dist)
                    distributions[(score, dice)] = dist


            unsolved_states = next_states
        return Policy(utilities, distributions, objective_func)

    def savePolicies(self, outfile="policies.json"):
        data = {name: p.to_json() for name, p in self.policies.items()}
        with open(outfile, "w") as fp:
            json.dump(data, fp)

    def addPolicy(self, name, func):
        self.policies[name] = self.computePolicy(func)

    def comparePolicies(self, name1, name2, games=100):
        p1, p2 = self.policies[name1], self.policies[name2]
        wins = np.zeros(games)
        turns_arr = np.zeros(games)
        for g in range(games):
            score1 = score2 = 0
            turns = 0
            while True:
                if score1 >= 1e4: break
                score1 += p1.simulateTurn()
                if score2 >= 1e4: break
                score2 += p2.simulateTurn()
                turns += 1
            wins[g] = score1 > score2
            turns_arr[g] = turns

        print(np.mean(wins), np.mean(turns_arr), np.median(turns_arr))

    @staticmethod
    def computeTransitions(outfile="farkle_transitions.json"):
        """This method is the base for all others - it simulates every possible roll. 

        In addition to supporting this class' nefarious purposes of farkle DOMINATION
        this is useful information in its own right. It can be used, for instance, to determine the expected max point value
        from a roll as well as the number of 
        """
        cache = {}
        repeats = {}
        for num_dice in range(2,7):
            print(num_dice)
            for roll in product(range(1,7), repeat=num_dice):
                key = tuple(sorted(roll))
                if key in cache:
                    repeats[key] += 1
                    continue
                options = score_roll(roll)
                cache[key] = options
                repeats[key] = 1

        with open(outfile, "w") as fp:
            json.dump({"options":list(cache.items()), "repeats":list(repeats.items())}, fp)

    @staticmethod
    def summarizeTransitions(infile="farkle_transitions.json", outfile="farkle_summarized_transitions.json"):
        # compact the results of the above method
        with open(infile, "r") as fp:
            data = json.load(fp)

        cached_repeats = {tuple(roll): reps for roll, reps in data["repeats"]}

        repeats = {i: {} for i in range(2,7)}

        for roll, options in data["options"]:
            num_dice = len(roll)
            reps = cached_repeats[tuple(roll)]
            options = tuple((score, dice) for score, dice in options)
            if options in repeats[num_dice]:
                repeats[num_dice][options] += reps
            else: repeats[num_dice][options] = reps

        for i in repeats:
            assert sum(repeats[i].values()) == 6**i
            print(i, len(repeats[i]))

        with open(outfile, "w") as fp:
            json.dump({i: list(repeats[i].items()) for i in repeats}, fp)

if __name__ == "__main__":
    #for test_roll in [(1,2,3,4,5,6), (2,2,4,4,5,5), (1,1,1,1,2,5), (2,2,2,1,5,3), (4,4,6,6,3,2)]:
    #    print(sorted(test_roll, score_roll(test_roll))
    #FarkleBot.summarizeTransitions()
    #bot = FarkleBot()
    #bot.savePolicies()
    bot = FarkleBot(policyFile="policies.json")
    #for cutoff in [800, 1100, 2000]:
    #    func = lambda dist: sum(prob if score >= cutoff else 0 for score, prob in dist.items())
    #    bot.addPolicy(f"take_{cutoff}", func)
    #bot.savePolicies()
    bot.comparePolicies("take_800", "take_500", games=1000)
    #policy = bot.policies["max_score"]
    #for dice_remaining in range(1,6):
    #    for score in range(0, 10**4, 50):
    #        if policy.should_stop(score, dice_remaining):
    #            print(score, dice_remaining)
    #            break
