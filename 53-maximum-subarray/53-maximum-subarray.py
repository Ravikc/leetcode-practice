class Solution:    
    def helper(self, nums, left, right, memo):
        if left > right or left < 0 or right >= len(nums):
            return 0
        
        key = f"{left}_{right}"
        if key in memo:
            return memo[key]
        
        if left == right:
            memo[key] = nums[left]
            return nums[left]
        
        memo[key] = nums[left] + nums[right] + self.helper(nums, left + 1, right - 1, memo)
        
        return memo[key]
        
    
    def maxSubArray_old(self, nums: List[int]) -> int:
        memo = {}
        ans = nums[0]
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i - 1, -1):                
               ans = max(ans, self.helper(nums, i, j, memo))
                       
        return ans   
    
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            ans = max(ans, dp[i])
            
        return ans