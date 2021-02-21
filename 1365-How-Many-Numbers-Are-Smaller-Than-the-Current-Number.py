class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums), 1):
            temp = 0
            for j in range(0, len(nums), 1):
                if i == j:
                    continue
                elif nums[i] > nums[j]:
                    temp += 1
            output.append(temp)
        return output
