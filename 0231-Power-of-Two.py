class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powerOfTwo = []
        for i in range(0, 101, 1):
            powerOfTwo.append(2**i)
        if n in powerOfTwo:
            return True
        else:
            return False
