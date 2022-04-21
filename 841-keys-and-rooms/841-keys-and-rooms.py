class Solution:
    def dfs(self, curr, graph, visited):
        if curr in visited:
            return
        
        visited.add(curr)
        for n in graph[curr]:
            self.dfs(n, graph, visited)
    
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(0, rooms, visited)
        
        return len(visited) == len(rooms)