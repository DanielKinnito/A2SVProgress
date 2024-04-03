class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for pre in prerequisites:
            courses[pre[1]].append(pre[0])
        
        unchecked, visited, dead = 1, 2, 3
        all_nodes = {i: unchecked for i in range(numCourses)}
        
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
            
            all_nodes[node] = visited

            if node in courses:
                for neighbor in courses[node]:
                    if all_nodes[neighbor] == unchecked:
                        dfs(neighbor)
                    elif all_nodes[neighbor] == visited:
                        no_cycle = False
            
            all_nodes[node] = dead
            
            
        for key in courses:
            dfs(key)
        
        return no_cycle