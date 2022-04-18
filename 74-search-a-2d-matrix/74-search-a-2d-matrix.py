class Solution:
    def helper(self, matrix, left, right, target):
        if left > right:
            return False        
       
        numCols = len(matrix[0])
        mid = left + ((right - left) // 2)
        row = mid // numCols
        col = mid % numCols
                
        if target == matrix[row][col]:
            return True
        
        if target < matrix[row][col]:
            return self.helper(matrix, left, mid - 1, target)
        
        return self.helper(matrix, mid + 1, right, target)
            
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.helper(matrix, 0, (len(matrix) * len(matrix[0])) - 1, target) 