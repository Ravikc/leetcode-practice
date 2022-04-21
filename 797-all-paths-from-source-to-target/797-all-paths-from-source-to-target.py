class Solution:
    def dfs(self, curr, target, graph, path, ans):
        if curr == target:
            ans.append([i for i in path])
            return
        
        for n in graph[curr]:
            path.append(n);
            self.dfs(n, target, graph, path, ans)
            path.pop()
    
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        ans = []
        path.append(0)
        self.dfs(0, len(graph) - 1, graph, path, ans)
        return ans