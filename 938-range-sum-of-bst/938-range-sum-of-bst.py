# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], lo: int, hi: int) -> int:
        if not root:
            return 0
        q = deque()
        ans = 0
        q.append(root)
        while q:
            count = len(q)
            for i in range(count):
                temp = q.popleft()
                if temp.val >= lo and temp.val <= hi:
                    ans += temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return ans