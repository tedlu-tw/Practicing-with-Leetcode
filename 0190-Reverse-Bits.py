class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(0, 32, 1):
            if n & 1:
                res += 1 << (31 - i)
            n >>= 1
        return res
