# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = len(inorder) - 1
        def helper(postorder, inorderIndices, left, right):
            if left > right:
                return None

            nonlocal index
            value = postorder[index]
            index -= 1
            root = TreeNode(value)
            inorderIndex = inorderIndices[value]
            root.right = helper(postorder, inorderIndices, inorderIndex + 1, right)
            root.left = helper(postorder, inorderIndices, left, inorderIndex - 1)
            return root
        
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        
        return helper(postorder, dic, 0, len(inorder) - 1)