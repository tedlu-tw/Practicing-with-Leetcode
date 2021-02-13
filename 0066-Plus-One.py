class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in range(0, len(digits), 1):
            string += str(digits[i])
        return list(str(int(string) + 1))
