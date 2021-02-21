class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        data = []
        for i in range(0, len(words), 1):
            w = words[i + 1:] + words[0:i]
            if words[i] in " ".join(w):
                data.append(words[i])
        return data
