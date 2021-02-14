class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0:
            num += 2 ** 32
        output = ""
        letter = "0123456789abcdef"
        while num > 0:
            output = letter[num % 16] + output
            num //= 16
        return output
