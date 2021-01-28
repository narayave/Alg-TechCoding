
# Leetcode - https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        def postorder(root, res):
            # print(root.val, res)

            if root.left:
                # print(f"l - {root.left.val}")
                res = postorder(root.left, res)

            if root.right:
                # print(f"r - {root.right.val}")
                res = postorder(root.right, res)

            res.append(root.val)

            return res

        return postorder(root, [])