class Solution:
    def helper(self, candidates, target, ans, currAns, currSum, index):
        if currSum > target:
            return
        
        if currSum == target:
            ans.append(currAns.copy())
            return
        
        for i in range(index, len(candidates)):
            currAns.append(candidates[i])
            self.helper(candidates, target, ans, currAns, currSum + candidates[i], i)
            currAns.pop()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        currAns = []
        
        self.helper(candidates, target, ans, currAns, 0, 0)
        return ans