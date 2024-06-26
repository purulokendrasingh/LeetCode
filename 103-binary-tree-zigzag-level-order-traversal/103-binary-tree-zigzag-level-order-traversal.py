# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        q = deque()
        q.append(root)
        ans = []
        rev = False
        while q:
            count = len(q)
            temp = []
            for _ in range(count):
                t = q.popleft()
                temp.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            if rev:
                temp = temp[::-1]
            ans.append(temp)
            rev = not rev
        return ans