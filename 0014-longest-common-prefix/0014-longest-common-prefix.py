class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs:
            return ''
        class TrieNode:
            def __init__(self):
                self.children = [None]*26
                self.isEOW = False
                
        def isEmpty(node):
            for k in node.children:
                if k != None:
                    return False
            return True
        
        def insert(node, key):
            for k in key:
                i = ord(k) - ord('a')
                if node.children[i] is None:
                    node.children[i] = TrieNode()
                node = node.children[i]
            node.isEOW = True
        
        root = TrieNode()
        for w in strs:
            insert(root, w)
            
        ans = ""
        node = root
        while not isEmpty(node):
            temp = []
            for i,k in enumerate(node.children):
                if k is not None:
                    temp.append(i)
            if len(temp) != 1:
                break
            elif len(temp) == 1:
                if not node.isEOW:
                    ans += chr(ord('a')+temp[0])
                    node = node.children[temp[0]]
                else:
                    break
        return ans