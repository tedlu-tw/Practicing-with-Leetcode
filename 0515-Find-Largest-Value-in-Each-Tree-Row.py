import collections

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        queue = collections.deque([root])
        ans = []
        while queue:
            temp = -2147483648
            tempQueue = collections.deque([])
            for node in list(queue):
                queue.popleft()
                temp = max(temp, node.val)
                if node.left:
                    tempQueue.append(node.left)
                if node.right:
                    tempQueue.append(node.right)
            queue = tempQueue
            ans.append(temp)
        return ans
