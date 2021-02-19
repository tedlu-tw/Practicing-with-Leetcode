import collections

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0:
                ret += remainders[0]
            else:
                ret += remainders[60 - t % 60]
            remainders[t % 60] += 1
        return ret
