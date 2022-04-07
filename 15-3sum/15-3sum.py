class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            targetSum = 0 - nums[i]
            lo = i + 1
            hi = len(nums) - 1
            
            while lo < hi:
                threeSum = nums[lo] + nums[hi]
                if threeSum == targetSum:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    
                    lo += 1
                    while lo < len(nums) and nums[lo] == nums[lo - 1]:
                        lo += 1
                    
                    hi -= 1
                    while hi > 0 and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif threeSum > targetSum:
                    hi -= 1
                else:
                    lo += 1
            
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
                
        return ans