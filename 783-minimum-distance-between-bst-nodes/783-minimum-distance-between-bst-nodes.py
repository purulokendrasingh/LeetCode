# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = -100000
        self.minn = 100000
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        def inorder(root):
            if root:
                inorder(root.left)
                if self.prev != None:
                    diff = root.val - self.prev
                    self.minn = min(self.minn, diff)
                self.prev = root.val
                inorder(root.right)
        
        inorder(root)
        return self.minn