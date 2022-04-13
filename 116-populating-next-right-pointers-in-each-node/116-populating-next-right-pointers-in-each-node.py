"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftmost = prev = curr = root
        while leftmost:
            while curr and curr.left:
                curr.left.next = curr.right
                if curr != prev:
                    prev.right.next = curr.left
                    prev = curr
                
                curr = curr.next
                
            curr = prev = leftmost = leftmost.left
            
        return root
                
