class Solution:
    
    
    def countVowelStrings(self, n: int) -> int:
        ans = 0
        def helper(vowels, arr, targetCount, index):
            nonlocal ans
            if len(arr) == targetCount:
                ans += 1
                return
                
            for i in range(index, len(vowels)):
                arr.append(vowels[i])
                helper(vowels, arr, targetCount, i)
                arr.pop()
                
        
        arr = []
        helper(['a', 'e', 'i', 'o', 'u'], arr, n, 0)
        return ans
