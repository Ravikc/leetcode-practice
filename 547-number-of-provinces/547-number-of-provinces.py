class Solution:
    def findRoot(self, roots, x):
        while roots[x] != x:
            x = roots[x]
            
        return x
    
    def union(self, roots, x, y):
        rootX = self.findRoot(roots, x)
        rootY = self.findRoot(roots, y)
        if rootX == rootY:
            return
        
        roots[rootY] = rootX
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        roots = [i for i in range(len(isConnected))]
        for i in range(0, len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    self.union(roots, i, j)
                  
        provinces = set([self.findRoot(roots, i) for i in range(len(isConnected))])
        return len(provinces)
        
            