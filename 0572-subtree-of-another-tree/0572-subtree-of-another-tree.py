# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p,q):
            if p is None and q is None:
                return True
            elif p is not None and q is not None and p.val == q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right):
                return True
            return False
        
        q = deque()
        q.append(root)
        while q:
            cnt = len(q)
            for _ in range(cnt):
                temp = q.popleft()
                if temp.val == subRoot.val and sameTree(temp, subRoot):
                    return True
                if temp.left:
                    q.append(temp.left)
                if temp.right: 
                    q.append(temp.right)
                
        return False