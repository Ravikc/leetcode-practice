class Solution:
    def climb(self, n, memo):
        if n < 3:
            return n
        
        if n not in memo:
            memo[n] = self.climb(n - 1, memo) + self.climb(n - 2, memo)
            
        return memo[n]
        
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climb(n, memo)