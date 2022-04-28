class Solution:
    def fibo(self, n, memo):
        if n < 2:
            return n
        
        if n not in memo:        
            memo[n] = self.fibo(n - 1, memo) + self.fibo(n - 2, memo)
            
        return memo[n]
    
    def fib(self, n: int) -> int:
        memo = {}
        return self.fibo(n, memo)