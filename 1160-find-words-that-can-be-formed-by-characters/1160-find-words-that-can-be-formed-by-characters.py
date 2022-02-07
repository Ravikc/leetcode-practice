class Solution:
    def getCharCountMap(self, word):
        charsMap = {}
        for char in word:
            if char in charsMap:
                charsMap[char] += 1
            else:
                charsMap[char] = 1
            
        return charsMap
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = self.getCharCountMap(chars)
        ans = 0
        for word in words:
            wordMap = {}
            match = True
            for char in word:
                if char in wordMap:
                    wordMap[char] += 1
                else:
                    wordMap[char] = 1
                    
                if char not in charsMap or wordMap[char] > charsMap[char]:
                    match = False
                
            if match:
                ans += len(word)
                
        return ans
        

            
                
            