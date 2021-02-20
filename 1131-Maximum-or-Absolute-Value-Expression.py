class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        res = 0
        for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            maxv = -4000000
            minv = 4000000
            for i in range(n):
                maxv = max(maxv, arr1[i] * dx + arr2[i] * dy + i)
                minv = min(minv, arr1[i] * dx + arr2[i] * dy + i)
            res = max(res, maxv - minv)
        return res
