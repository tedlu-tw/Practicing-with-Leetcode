class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        for word in reversed((words)):
            if word: 
                return len(word)
        return 0
