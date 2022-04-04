class Solution:
    def swap(self, nums, left, right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        
        while left < len(nums) and nums[left] == 0:
            left += 1
        
        while right >= 0 and nums[right] == 2:
            right -= 1
            
        curr = left
        while curr <= right:
            swapped = False
            if nums[curr] == 0 and curr >= left:
                self.swap(nums, left, curr)
                swapped = True                
            
            if nums[curr] == 2:
                self.swap(nums, curr, right)
                swapped = True
                
                    
            while left < len(nums) and nums[left] == 0:
                left += 1
            
            while right >= 0 and nums[right] == 2:
                right -= 1
            
            # curr += 1
            if not swapped:
                curr += 1
            # else:
            #     curr = left