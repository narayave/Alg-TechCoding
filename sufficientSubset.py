
# Leetcode mock interview - https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        if not root:
            return None
        if not root.left and not root.right:
            if root.val < limit:
                return None
            else:
                return root

        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)

        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)

        return root if root.left or root.right else None
