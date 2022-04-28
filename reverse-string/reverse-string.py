class Solution:
    def reverse(self, s, l, r):
        if l > r:
            return
        
        s[l], s[r] = s[r], s[l]    
        self.reverse(s, l + 1, r - 1)
        
        
        
    def reverseString(self, s: List[str]) -> None:
        self.reverse(s, 0, len(s) - 1)
        