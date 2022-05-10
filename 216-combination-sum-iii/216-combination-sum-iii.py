class Solution:
    def findSum(self, target, count, ans, currAns, currSum, currNum):
        if len(currAns) == count:
            if currSum == target:                
                ans.append(currAns.copy())
                
            return
        
        for i in range(currNum, 10):
            currAns.append(i)
            self.findSum(target, count, ans, currAns, currSum + i, i + 1)
            currAns.pop()
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        currAns = []
        self.findSum(n, k, ans, currAns, 0, 1)
        return ans