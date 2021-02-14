class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s), 1):
            if s.count(s[i]) == 1:
                return s.index(s[i])
        return -1
