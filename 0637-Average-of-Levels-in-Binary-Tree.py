# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        output = []
        queue = [root]
        while queue:
            level_sum, level_count = 0, len(queue)
            for i in range(level_count):
                node = queue.pop(0)
                level_sum += node.val
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            output.append(level_sum / level_count)
        return output
