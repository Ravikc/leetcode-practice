class Solution:
    def findLeft(self, arr, lo, hi, target):
        if lo > hi:
            return None
        
        mid = ((hi - lo) // 2) + lo
        if arr[mid] == target:
            moreLeft = self.findLeft(arr, lo, mid - 1, target)            
            return min(mid, moreLeft if (moreLeft or moreLeft == 0) else mid)
        elif arr[lo] <= target and target <= arr[mid]:
            return self.findLeft(arr, lo, mid - 1, target)
        elif arr[hi] >= target and target >= arr[mid]:
            return self.findLeft(arr, mid + 1, hi, target)
        else:
            return None
        
    def findRight(self, arr, lo, hi, target):
        if lo > hi:
            return None
        
        mid = ((hi - lo) // 2) + lo
        if arr[mid] == target:
            moreRight = self.findRight(arr, mid + 1, hi, target)
            return max(mid, moreRight if (moreRight or moreRight == 0) else mid)
        elif arr[lo] <= target and target <= arr[mid]:
            return self.findRight(arr, lo, mid - 1, target)
        # elif arr[hi] >= target and target >= arr[mid]:
        else:
            return self.findRight(arr, mid + 1, hi, target)
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeft(nums, 0, len(nums) - 1, target)
        if left == None:
            return [-1, -1]
        
        right = self.findRight(nums, 0, len(nums) - 1, target)
        return [left, right]