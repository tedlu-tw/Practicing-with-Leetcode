class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums), 1):
            for j in range(0, len(nums), 1):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i, j]
