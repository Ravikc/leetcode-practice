# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val <= low:
            root.left = None
        else:
            root.left = self.trimBST(root.left, low, high)
        
        if root.val >= high:
            root.right = None
        else:
            root.right = self.trimBST(root.right, low, high)
       
        
        
        if low <= root.val and root.val <= high:
            return root
        elif root.left is not None:
            return root.left
        else:
            return root.right