class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for index in range(len(flowerbed)):
            canPlant = True
            if flowerbed[index] == 1:
                canPlant = False
            if index > 0 and flowerbed[index - 1] == 1:
                canPlant = False
            if index < len(flowerbed) - 1 and flowerbed[index + 1] == 1:
                canPlant = False
                
            if canPlant:
                flowerbed[index] = 1
                n -= 1
        
        return n <= 0
        
        
        