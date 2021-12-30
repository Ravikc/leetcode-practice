class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
        
        for char in t:
            if char not in dic:
                return False
            dic[char] -= 1
        
        for value in dic.values():
            if value != 0:
                return False
        
        return True