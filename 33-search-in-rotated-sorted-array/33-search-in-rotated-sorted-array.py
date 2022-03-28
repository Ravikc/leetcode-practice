class Solution:
    def helper(self, nums, target, lo, hi):
        if hi < lo:
            return -1
        
        mid = ((hi - lo) // 2) + lo
        if nums[mid] == target:
            return mid
        
        leftSorted = nums[lo] <= nums[mid]
        rightSorted = nums[mid] < nums[hi]
        
        if leftSorted and target >= nums[lo] and target < nums[mid]:
            return self.helper(nums, target, lo,  mid - 1)
        elif rightSorted and target <= nums[hi] and target > nums[mid]:
            return self.helper(nums, target, mid + 1, hi)
        else:
            if leftSorted:
                return self.helper(nums, target, mid + 1, hi)
            else:
                return self.helper(nums, target, lo,  mid - 1)
        
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)
        