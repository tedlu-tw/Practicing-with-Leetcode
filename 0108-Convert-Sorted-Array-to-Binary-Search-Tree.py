class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def devide(nums):
            if len(nums) == 0:
                return None
            midPoint = len(nums) // 2
            left_list = nums[:midPoint]
            right_list = nums[midPoint+1:]
            return TreeNode(nums[midPoint], devide(left_list), devide(right_list))
        return devide(nums)
