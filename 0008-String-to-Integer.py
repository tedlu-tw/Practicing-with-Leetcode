import re

class Solution:
    def myAtoi(self, s: str) -> int:
        numString = re.findall("^[\+\-]?\d+", s.strip()) 
        if len(numString) == 0:
            return 0
        if int(numString[0]) > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif int(numString[0]) < pow(-2, 31):
            return pow(-2, 31)
        else:
            return int(numString[0])
