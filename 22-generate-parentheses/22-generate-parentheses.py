class Solution:
    def isValid(self, braces):
        # print("checking for", "".join(braces))
        if len(braces) == 0 or braces[0] == ")" or braces[-1] == "(":
            return False
        
        stack = []
        for brace in braces:
            if len(stack) > 0 and brace == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(brace)
                
        return len(stack) == 0
                    
        
    def helper(self, n, braces, ans):
        if len(braces) == n * 2:
            if self.isValid(braces):
                ans.append("".join(braces))
            
            return
        
        braces.append("(")
        self.helper(n, braces, ans)
        braces.pop()
        
        if len(braces) > 0:
            braces.append(")")
            self.helper(n, braces, ans)
            braces.pop()
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        braces = []
        ans = []
        self.helper(n, braces, ans)
        return ans