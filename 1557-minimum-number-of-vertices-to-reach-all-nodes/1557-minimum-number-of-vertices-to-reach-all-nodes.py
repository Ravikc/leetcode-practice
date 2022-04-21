class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0 for i in range(n)]
        for edge in edges:
            indegree[edge[1]] += 1
            
        ans = []
        for i, num in enumerate(indegree):
            if num == 0:
                ans.append(i)
                
        return ans
        