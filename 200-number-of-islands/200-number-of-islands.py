class Solution:
    def dfs(self, grid, row, col, numRows, numCols, visited):
        if row < 0 or row >= numRows or col < 0 or col >= numCols or grid[row][col] == '0':
            return
        
        key = f"{row}_{col}"
        if key in visited:
            return
        
        visited.add(key)
        self.dfs(grid, row + 1, col, numRows, numCols, visited)
        self.dfs(grid, row - 1, col, numRows, numCols, visited)

        self.dfs(grid, row, col + 1, numRows, numCols, visited)
        self.dfs(grid, row, col - 1, numRows, numCols, visited)


    
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        visited = set()
        ans = 0
        
        for i in range(numRows):
            for j in range(numCols):
                count = len(visited)
                self.dfs(grid, i, j, numRows, numCols, visited)
                if count < len(visited):
                    ans += 1
                    
        return ans