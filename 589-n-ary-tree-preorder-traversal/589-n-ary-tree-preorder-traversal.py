"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, node, ans):
        if node is None:
            return
        
        ans.append(node.val)
        for child in node.children:
            self.traverse(child, ans)
    
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.traverse(root, ans)
        
        return ans
        
        