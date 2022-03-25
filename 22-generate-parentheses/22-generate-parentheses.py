class Solution:
        
    def helper(self, n, braces, ans, remainingOpen, remainingClose):
        if len(braces) == n * 2:
            ans.append("".join(braces))
            
            return
        
        if remainingOpen > 0:
            braces.append("(")
            self.helper(n, braces, ans, remainingOpen - 1, remainingClose)
            braces.pop()
        
        appliedOpeningBraces = n - remainingOpen
        appliedClosingBraces = n - remainingClose
        if len(braces) > 0 and remainingClose > 0 and appliedOpeningBraces > appliedClosingBraces:
            braces.append(")")
            self.helper(n, braces, ans, remainingOpen, remainingClose - 1)
            braces.pop()
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        braces = []
        ans = []
        self.helper(n, braces, ans, n, n)
        return ans