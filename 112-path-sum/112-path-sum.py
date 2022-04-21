# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, currSum, targetSum):
        if not node:
            return False
        
        if not node.left and not node.right:
            return currSum + node.val == targetSum
        
        
        return self.helper(node.left, currSum + node.val, targetSum) or self.helper(node.right, currSum + node.val, targetSum)
        
    
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        return self.helper(root, 0, targetSum)
        
        