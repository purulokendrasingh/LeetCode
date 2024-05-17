# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(node, prev, left):
            if node:
                helper(node.left, node, True)
                helper(node.right, node, False)
                if not node.left and not node.right and node.val == target and prev is not None:
                    if left:
                        prev.left = None
                    else:
                        prev.right = None
            
        helper(root, None, False)
        if not root.left and not root.right and root.val == target:
            return None
        return root
                    