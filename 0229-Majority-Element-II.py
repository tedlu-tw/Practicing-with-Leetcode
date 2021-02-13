class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val = len(nums) / 3
        output = []
        for i in range(0, len(nums), 1):
            if nums == []:
                break
            elif nums.count(nums[0]) > val:
                output.append(nums[0])
                data = nums[0]
                for i in range(0, nums.count(nums[0]), 1):
                    nums.remove(data)
            else:
                data = nums[0]
                nums.remove(data)
        return output
