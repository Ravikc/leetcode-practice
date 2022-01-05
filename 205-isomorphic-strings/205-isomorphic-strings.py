class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        isGettingReplacedByMap = {}
        replacesMap = {}
        for index in range(len(s)):
            sChar = s[index]
            tChar = t[index]
            
            if sChar not in isGettingReplacedByMap:
                if tChar not in replacesMap or replacesMap[tChar] == sChar:
                    isGettingReplacedByMap[sChar] = tChar
                    replacesMap[tChar] = sChar
                else:
                    return False
            else:
                if isGettingReplacedByMap[sChar] != tChar:
                    return False
            
        
        return True
        