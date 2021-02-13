class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 1):
            if nums.count(nums[i]) > 1:
                continue
            else:
                return nums[i]
