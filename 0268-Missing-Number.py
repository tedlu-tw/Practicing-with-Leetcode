class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = list(range(0, len(nums), 1))
        for i in range(0, len(nums), 1):
            if nums[i] in arr:
                arr.remove(nums[i])
            else:
                continue
        try:
            return arr[0]
        except IndexError:
            return max(nums) + 1
