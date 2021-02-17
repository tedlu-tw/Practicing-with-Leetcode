class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        total = sum(A)
        for i in range(0, len(A), 1): 
            A[i] = len(A) * A[i] - total
        A.sort()
        X = set()
        for a in A[:-1]:
            X |= {a} | {a + x for x in X if x < 0}
            if 0 in X: 
                return True
        return False
