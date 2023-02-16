# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        ans = 0
        while q:
            count = len(q)
            ans += 1
            for i in range(count):
                temp = q.popleft()
                if temp.right:
                    q.append(temp.right)
                if temp.left:
                    q.append(temp.left)
        return ans