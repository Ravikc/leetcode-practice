class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        ans = []
        left = 0
        intervals.sort(key=lambda x: x[0])
        largestEndSoFar = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= largestEndSoFar:
                largestEndSoFar = max(largestEndSoFar, intervals[i][1])
                continue
            
            largestEndSoFar = intervals[i][1]
            smallest = intervals[left][0]
            largest = intervals[left][1]
            for j in range(left, i):
                largest = max(largest, intervals[j][1])
            
            ans.append([smallest, largest])
            left = i
        
        smallest = intervals[left][0]
        largest = intervals[left][1]
        for j in range(left, len(intervals)):
            largest = max(largest, intervals[j][1])
        
        ans.append([smallest, largest])
        
        return ans;
            
            