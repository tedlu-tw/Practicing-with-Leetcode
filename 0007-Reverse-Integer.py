class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31 - 1:
            return 0
        elif x < 0:
            if int("-" + str(x).replace("-", "")[::-1]) < -2**31 or int("-" + str(x).replace("-", "")[::-1]) > 2**31 - 1:
                return 0
            else:
                return int("-" + str(x).replace("-", "")[::-1])
        else:
            if int(str(x)[::-1]) < -2**31 or int(str(x)[::-1]) > 2**31 - 1:
                return 0
            else:
                return int(str(x)[::-1])
