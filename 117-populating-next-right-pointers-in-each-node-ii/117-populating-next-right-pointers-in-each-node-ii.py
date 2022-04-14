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
        leftmost = prev = curr = root
        while leftmost:
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                
                if curr != prev:
                    fromNode = prev.right or prev.left
                    toNode = curr.left or curr.right
                    if fromNode:
                        fromNode.next = toNode
                    if toNode:
                        prev = curr
                        
                curr = curr.next
            
            while leftmost:
                newleftmost = leftmost.left or leftmost.right
                if newleftmost:
                    leftmost = newleftmost
                    break
                leftmost = leftmost.next
                
            curr = prev = leftmost
            
        return root