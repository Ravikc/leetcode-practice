class Solution:
    def addOneToDiff(self, diff, c):
        if c not in diff:
            diff[c] = 0
        
        diff[c] += 1
        if diff[c] == 0:
            del diff[c]
    
    def removeOneFromDiff(self, diff, c):
        if c not in diff:
            diff[c] = 0
        
        diff[c] -= 1
        if diff[c] == 0:
            del diff[c]
    
    
    def getDiff(self, s, p):
        diff = {}
        for i in range(len(p)):
            self.addOneToDiff(diff, s[i])
            
        for c in p:
            self.removeOneFromDiff(diff, c)
                
        return diff
    
    
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        if len(s) < len(p):
            return []
        
        left = 0
        right = len(p) - 1
        ans = []
        diff = self.getDiff(s, p)
        # print(diff)
        while right < len(s):
            if len(diff) == 0:
                ans.append(left)
                
            if right + 1 < len(s):
                self.addOneToDiff(diff, s[right + 1])
                
            self.removeOneFromDiff(diff, s[left])
            left += 1
            right += 1
            
        return ans