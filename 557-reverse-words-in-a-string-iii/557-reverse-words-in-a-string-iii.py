class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        left = 0
        right = 0
        
        while right < len(s):
            while right < len(s) - 1 and not s[right].isspace():
                right += 1
                            
            if s[right].isspace():
                right -= 1
                
            wordLength = right - left
            for index in range(right, left - 1, -1):
                ans.append(s[index])
            
            ans.append(' ')
                
            right += 2
            left = right
            
        ans.pop()
        return "".join(ans)