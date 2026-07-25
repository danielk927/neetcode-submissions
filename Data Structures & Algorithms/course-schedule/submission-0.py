class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a, b in prerequisites: 
            adjList[a].append(b)

        visiting = set() 
        visited = set() 

        def dfs(node):
            if node in visiting: 
                return False
            if node in visited: 
                return True
            visiting.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i): 
                return False
        return True
        



