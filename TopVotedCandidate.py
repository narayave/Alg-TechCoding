
# Leetcode mock interview - https://leetcode.com/problems/online-election/

# NOT WORKING
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.candidates = list(set(self.persons))
        self.voteTimes = defaultdict(lambda: defaultdict(lambda: 0))
        self.process()


    def process(self) -> None:

        for i, t in enumerate(self.times):

            # vote = self.persons[i]
            # self.voteTimes[t][vote] += 1
            if i > 0:
                for c in self.candidates:
                    self.voteTimes[t][c] += self.voteTimes[self.times[i-1]][c]

            vote = self.persons[i]
            self.voteTimes[t][vote] += 1

            recent = vote
            prevrecent = self.persons[i-1]
            localmax = 0
            curmaxid = -1
            dups = []
            for ca in self.candidates:
                if self.voteTimes[t][ca] > localmax:
                    localmax = self.voteTimes[t][ca]
                    curmaxid = ca
                    dups = [ca]
                elif self.voteTimes[t][ca] == localmax and self.voteTimes[t][c] > 0:
                    dups.append(ca)
            print(localmax, curmaxid, dups)
            if not dups:
                self.voteTimes[t][-1] = curmaxid
            else:
                self.voteTimes[t][-1] = recent if recent in dups else prevrecent

        for v in self.voteTimes:
            print(v, self.voteTimes[v])


    def q(self, t: int) -> int:

        prev=None
        time = None
        for k in self.voteTimes:

            if t < k:
                continue
            elif t > k:
                prev = k
            elif t == k:
                time = k
                break

        if time:
            return self.voteTimes[time][-1]
        else:
            return self.voteTimes[prev][-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)