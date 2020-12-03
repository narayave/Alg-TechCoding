# Leetcode - https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # this was too slow
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        return self._helper([root])

    def _helper(self, innodes, res=[]):

        local_res = []
        parent = []

        if innodes == []:
            return res
        # print(len(innodes))
        for node in innodes:
            parent.append(node.val)
            if node.left:
                local_res.append(node.left)
            if node.right:
                local_res.append(node.right)

        print(parent)
        print(local_res)
        print(res)
        print()
        final_result = res + [parent]
        print(final_result)

        return self._helper(innodes=local_res, res=final_result)



# Better
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        q = [root]

        while q:

            local_res = []

            for i in range(len(q)):
                node = q[0]
                q = q[1:]
                local_res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += [local_res]

        return res


