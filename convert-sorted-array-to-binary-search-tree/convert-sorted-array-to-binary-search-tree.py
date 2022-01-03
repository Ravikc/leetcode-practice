# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getBst(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return None
        
        mid = int(left + ((right - left) / 2))
        leftBst = self.getBst(nums, left, mid - 1)
        rightBst = self.getBst(nums, mid + 1, right)
        
        return TreeNode(nums[mid], leftBst, rightBst)
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getBst(nums, 0, len(nums) - 1)
        
    
        