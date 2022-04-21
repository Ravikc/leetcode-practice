class Solution:
    def getGraph(self, deps, n):
        graph = {}
        for i in range(n):
            graph[i] = []
        
        
        for dep in deps:
            graph[dep[0]].append(dep[1])
            
        return graph
        
    def hasCycle(self, inprogress, done, graph, curr):
        if curr in done:
            return False
        if curr in inprogress:
            return True
        
        inprogress.add(curr)
        for n in graph[curr]:
            if self.hasCycle(inprogress, done, graph, n):
                return True
            
        inprogress.remove(curr)
        done.add(curr)
        return False
        
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        done = set()
        inprogress = set()
        graph = self.getGraph(prerequisites, numCourses)
        
        for i in graph:
            print(i)
            if self.hasCycle(inprogress, done, graph, i):
                return False
            
        return True