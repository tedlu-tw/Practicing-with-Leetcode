class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        for i in range(3, n, 2):
            for p in primes:
                if p * p > i:
                    primes.append(i)
                    break
                if not i % p:
                    break                
        return len(primes)
