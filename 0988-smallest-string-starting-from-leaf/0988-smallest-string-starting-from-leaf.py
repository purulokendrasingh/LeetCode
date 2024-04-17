# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append([root, []])
        ans = []
        
        def is_leaf_node(node):
            return node and not node.left and not node.right
        
        def i2c(val):
            return chr(ord('a') + val)
        
        while q:
            cnt = len(q)
            for _ in range(cnt):
                node, res = q.popleft()
                res.append(i2c(node.val))
                if is_leaf_node(node):
                    ans.append(''.join(res[::-1]))
                else:
                    if node.left:
                        q.append([node.left, res.copy()])
                    if node.right:
                        q.append([node.right, res.copy()])
        
        ans.sort()
        return ans[0]