# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        temp = []
        
        def inorder(root):
            if root and not root.left and not root.right:
                temp.append(root.val)
            elif root:
                inorder(root.left)
                inorder(root.right)
                
        inorder(root1)
        a = temp
        print(a)
        temp = []
        inorder(root2)
        print(temp)
        return a == temp
                