
# Leetcode - https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        node = self.root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:

        curr = self.stack.pop()
        n = curr.right
        while n:
            self.stack.append(n)
            n = n.left
        return curr.val

    def hasNext(self) -> bool:

        if self.stack:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()