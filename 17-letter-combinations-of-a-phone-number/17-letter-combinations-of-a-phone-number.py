class Solution:
    def helper(self, arrs, indices, ans):
        if any(index < 0 for index in indices):
            return
        
        alphabets = []
        for arrNum in range(len(arrs)):
            alphabets.append(arrs[arrNum][indices[arrNum]])
         
        if len(alphabets) > 0:
            ans.add("".join(alphabets))
        
        for arrNum in range(len(arrs)):
            indices[arrNum] -= 1
            self.helper(arrs, indices, ans)
            indices[arrNum] += 1
    
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        
        arrs = []
        indices = []
        ans = set()
        for digit in digits:
            alphabets = dic[digit]
            arrs.append(list(alphabets))
            indices.append(len(alphabets) - 1)
            
        self.helper(arrs, indices, ans)
        return ans
        