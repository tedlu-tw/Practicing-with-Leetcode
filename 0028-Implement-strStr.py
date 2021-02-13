class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack and needle:
            try:
                return haystack.index(needle)
            except ValueError:
                return -1
        else:
            return 0
