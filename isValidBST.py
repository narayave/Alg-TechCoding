
# Leetcode - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def val(root, low=-math.inf, high=math.inf) -> bool:

            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False

            # For left branch, current value becomes the high
            # For right branch, current value becomes the lowest it can be
            return val(root.left, low, root.val) and val(root.right, root.val, high)

        return val(root)