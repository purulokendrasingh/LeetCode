# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque(), deque()
        q1.append(p)
        q2.append(q)
        while q1 or q2:
            c1 = len(q1)
            c2 = len(q2)
            temp1 = []
            for _ in range(c1):
                node1 = q1.popleft()
                if node1 is None:
                    temp1.append(None)
                    continue
                temp1.append(node1.val)
                q1.append(node1.left)
                q1.append(node1.right)
            
            temp2 = []
            for _ in range(c2):
                node2 = q2.popleft()
                if node2 is None:
                    temp2.append(None)
                    continue
                temp2.append(node2.val)
                q2.append(node2.left)
                q2.append(node2.right)

            if temp1 != temp2:
                return False
        return True