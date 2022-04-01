class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
                
            wordHash = "".join(str(num).zfill(3) for num in arr)
            if wordHash in dic:
                dic[wordHash].append(word)
            else:
                dic[wordHash] = [word]
                
        return dic.values()