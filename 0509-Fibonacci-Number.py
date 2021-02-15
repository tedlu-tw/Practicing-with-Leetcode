class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return a 
        if n == 1:
            return b
        n -= 2
        while n >= 0:
            a, b = b, a + b
            n -= 1
        return b
