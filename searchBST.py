
# Leetcode - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def find(root):

            if not root:
                return
            elif root.val == val:
                return root
            elif root.val > val:
                return find(root.left)
            elif root.val < val:
                return find(root.right)

        return find(root)