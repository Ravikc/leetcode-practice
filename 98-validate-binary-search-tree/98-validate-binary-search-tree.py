# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        stack = []
        
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
                
            node = stack.pop()
            if prev is not None and prev >= node.val:
                return False
            
            prev = node.val
            root = node.right
            
        return True
    