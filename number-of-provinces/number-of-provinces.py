class Solution:
    def findRoot(self, roots, x):
        if roots[x] == x:
            return x
        
        roots[x] = self.findRoot(roots, roots[x])
        return roots[x]
        
       
    
    def union(self, roots, ranks, x, y):
        rootX = self.findRoot(roots, x)
        rootY = self.findRoot(roots, y)
        if rootX == rootY:
            return
        
        if ranks[rootX] > ranks[rootY]:
            roots[rootY] = rootX
        elif ranks[rootX] < ranks[rootY]:
            roots[rootX] = rootY
        else:
            roots[rootY] = rootX
            ranks[rootX] += 1
        
        
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        roots = [i for i in range(len(isConnected))]
        ranks = [1 for i in range(len(isConnected))]
        for i in range(0, len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    self.union(roots, ranks, i, j)
                  
        provinces = set([self.findRoot(roots, i) for i in range(len(isConnected))])
        return len(provinces)
        
            