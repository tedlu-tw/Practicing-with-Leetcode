class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root, val):
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = insert(root.left,val)
            else:
                root.right = insert(root.right,val)
            return root
        return insert(root, val)
