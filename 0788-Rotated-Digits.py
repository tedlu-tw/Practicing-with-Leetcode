class Solution:
    def rotatedDigits(self, N: int) -> int:
        output = 0
        for i in range(0, N + 1, 1):
            s = str(i)
            if s.count("3") == 0 and s.count("4") == 0 and s.count("7") == 0:
                if s.count("1") + s.count("8") + s.count("0") != len(s):
                    output += 1
        return output
