
# Leetcode mock interview - https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        h = collections.defaultdict(tuple)

        que = [(root, 0, 0)]

        while que:

            item, level, parent = que.pop(0)
            h[item.val] = (level, parent)


            if item.left: que.append((item.left, level+1, item.val))
            if item.right: que.append((item.right, level+1, item.val))


        if h[x][0]==h[y][0] and h[x][1] != h[y][1]:
            return True

        return False



