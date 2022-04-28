class Solution:
    def searchBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not node or node.val == val:
            return node
  
        if val < node.val:
            return self.searchBST(node.left, val)
        
        return self.searchBST(node.right, val)