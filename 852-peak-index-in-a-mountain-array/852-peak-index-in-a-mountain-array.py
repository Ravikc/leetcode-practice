class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max = arr[1]
        maxIndex = 1
        for index in range(1, len(arr) - 1, 1):
            if arr[index] < max:
                return maxIndex
            elif arr[index] > max:
                max = arr[index]
                maxIndex = index
        
        return maxIndex
        