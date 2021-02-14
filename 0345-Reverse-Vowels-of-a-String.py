class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        word = ""
        vowels = "aeiouAEIOU"
        for i in s:
            if i in vowels :
                stack.append(i)
        for i in s:
            if i in vowels:
                word += stack.pop()
            else:
                word += i
                
        return word
