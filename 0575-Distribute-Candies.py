class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        length = len(candyType) / 2
        candySet = set(candyType)
        if len(candySet) < length:
            return len(candySet)
        else:
            return int(length)
