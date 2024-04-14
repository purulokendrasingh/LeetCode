# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append([root, False])
        res = 0
        while q:
            cnt = len(q)
            for _ in range(cnt):
                temp, flag = q.pop()
                if temp.left:
                    q.append([temp.left, True])
                if temp.right:
                    q.append([temp.right, False])
                if not temp.left and not temp.right and flag:
                    res += temp.val
        return res