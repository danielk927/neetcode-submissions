class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:    
        adjList = defaultdict(list)
        for a, b in edges: 
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set() 
        count = 0

        def bfs(node): 
            visited.add(node)
            q = collections.deque()
            q.append(node)

            while q: 
                currnode = q.popleft()
                for nei in adjList[currnode]:
                    if nei not in visited: 
                        visited.add(nei) 
                        q.append(nei)

        for node in range(n): 
            if node in visited: 
                continue 
            count += 1 
            bfs(node)
        return count 

