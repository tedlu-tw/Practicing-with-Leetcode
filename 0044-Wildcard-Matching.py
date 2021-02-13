class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        if not p:
            return False
        level = {0}
        for i, c in enumerate(p):
            if not level:
                return False
            
            if c == "*":
                level = set(range(min(level), len(s) + 1))
            else:
                level = {j + 1 for j in level if j < len(s) and (s[j] == c or c == "?")}
        
        return len(s) in level
