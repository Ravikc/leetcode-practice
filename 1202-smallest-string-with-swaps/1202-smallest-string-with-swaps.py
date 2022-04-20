class Solution:
    def findRoot(self, roots, x):
        if roots[x] == x:
            return x;
        
        roots[x] = self.findRoot(roots, roots[x])
        return roots[x]
    
    def union(self, roots, ranks, x, y):
        rootX = self.findRoot(roots, x)
        rootY = self.findRoot(roots, y)
        if rootX == rootY:
            return
        
        roots[rootY] = rootX
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        roots = [i for i in range(len(s))]
        ranks = [1 for i in range(len(s))]
        
        for pair in pairs:
            self.union(roots, ranks, pair[0], pair[1])
        
        dic = {}
        for i, val in enumerate(roots):
            root = self.findRoot(roots, val)
            if root not in dic:
                dic[root] = []
                
            dic[root].append(i)
          
        ans = ['0' for i in range(len(s))]
        for key in dic:
            chars = []
            for index in dic[key]:
                chars.append(s[index])
                
            i = 0
            chars.sort()
            for index in dic[key]:
                ans[index] = chars[i]
                i += 1
                
        
        return "".join(ans)
        