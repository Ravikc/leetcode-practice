class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxArr = [1] * len(nums)
        minArr = [1] * len(nums)
        maxArr[0] = minArr[0] = nums[0]
        
        for i in range(1, len(nums)):
            minArr[i] = min(nums[i], min(minArr[i - 1] * nums[i], maxArr[i - 1] * nums[i]))
            maxArr[i] = max(nums[i], max(maxArr[i - 1] * nums[i], minArr[i - 1] * nums[i]))
          
        return max(maxArr)