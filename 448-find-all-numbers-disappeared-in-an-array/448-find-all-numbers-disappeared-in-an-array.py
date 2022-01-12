class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            value = abs(nums[index])
            if nums[value - 1] > 0:
                nums[value - 1] = 0 - nums[value - 1]
        
        ans = []
        for index in range(len(nums)):
            if nums[index] > 0:
                ans.append(index + 1)
                
        return ans