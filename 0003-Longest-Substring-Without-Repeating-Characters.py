class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastPos = {}
        start = maxLen = 0
        for i, ch in enumerate(s):
            if ch in lastPos and lastPos[ch] >= start:
                start = lastPos[ch] + 1
            lastPos[ch] = i
            maxLen = max(maxLen, i - start + 1)
        return maxLen
