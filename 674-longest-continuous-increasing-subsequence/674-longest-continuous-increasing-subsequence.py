class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        curr = 1
        
        for index in range(1, len(nums), 1):
            if nums[index] > nums[index - 1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
                
        return ans