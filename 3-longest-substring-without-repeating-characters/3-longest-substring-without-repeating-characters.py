class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = ans = 0
        
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                ans = max(ans, len(seen))
            else:
                while s[right] in seen and left < right:
                    seen.remove(s[left])
                    left += 1
                    
                seen.add(s[right])
                right += 1
                ans = max(ans, len(seen))
                
        return ans
        