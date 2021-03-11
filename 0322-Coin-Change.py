from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        seen = set()
        q = deque([[0,0]])
        while q:
            curr, level = q.popleft()
            if level != 0 and curr == amount:
                return level
            for c in coins:
                if curr + c not in seen and curr + c <= amount:
                    q.append([curr + c, level + 1])
                    seen.add(curr + c)
        return -1
