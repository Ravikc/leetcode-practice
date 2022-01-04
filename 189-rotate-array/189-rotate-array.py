class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        startIndex = 0
        index = 0
        replaced = 0
        temp = nums[0]
        
        while replaced < len(nums):
            if startIndex == index and replaced > 0:
                startIndex += 1
                index = startIndex
                temp = nums[index]
            
            index = (index + k) % len(nums)
            temp2 = nums[index]
            nums[index] = temp
            temp = temp2
            replaced += 1
        
        
        