import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = nums1 + nums2
        data = sorted(data)
        if len(data) % 2 != 0:
            return data[math.ceil(len(data)/2) - 1]
        else:
            return (data[int(len(data) / 2 - 1)] + data[int(len(data) / 2)]) / 2
