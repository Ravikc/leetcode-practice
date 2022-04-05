# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, inorder, postorder, inorderIndices, left, right):
        if left > right:
            return None
        
        value = postorder.pop()
        root = TreeNode(value)
        inorderIndex = inorderIndices[value]
        root.right = self.helper(inorder, postorder, inorderIndices, inorderIndex + 1, right)
        root.left = self.helper(inorder, postorder, inorderIndices, left, inorderIndex - 1)
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        
        return self.helper(inorder, postorder, dic, 0, len(inorder) - 1)