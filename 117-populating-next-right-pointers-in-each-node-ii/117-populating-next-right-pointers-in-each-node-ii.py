"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            count = len(queue)
            prev = None
            
            for i in range(count):
                node = queue.popleft()
                if prev:
                    prev.next = node                
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                prev = node
                
        return root