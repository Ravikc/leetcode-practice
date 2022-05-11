class Solution:
    
    
    def countVowelStrings(self, n: int) -> int:
        ans = 0
        def helper(vowels, currCount, targetCount, index):
            nonlocal ans
            if currCount == targetCount:
                ans += 1
                return
                
            for i in range(index, len(vowels)):                
                helper(vowels, currCount + 1, targetCount, i)
                
        
        arr = []
        helper(['a', 'e', 'i', 'o', 'u'], 0, n, 0)
        return ans
