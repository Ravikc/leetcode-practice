class Solution:
    def helper(self, nums, curr, ans, visited):
        if len(curr) == len(nums):
            ans.append(curr.copy())
            return
        
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                curr.append(nums[i])
                self.helper(nums, curr, ans, visited)
                visited.remove(i)
                curr.pop()
                
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        ans = []
        visited = set()
        self.helper(nums, curr, ans, visited)
        return ans