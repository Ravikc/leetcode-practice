class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]        
       
        prevRow = self.getRow(rowIndex - 1)
        thisRow = [1]
        for i in range(1, rowIndex):
            thisRow.append(prevRow[i - 1] + prevRow[i])
            
        thisRow.append(1)
        return thisRow
        