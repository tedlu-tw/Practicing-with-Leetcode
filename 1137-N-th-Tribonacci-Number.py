class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        if n < 3:
            return 1
        i = 3
        while i <= n:
            a, b, c = b, c, a + b + c
            i += 1
        return c
