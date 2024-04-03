class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for pre in prerequisites:
            if pre[1] in courses:
                courses[pre[1]].append(pre[0])
            else:
                courses[pre[1]] = [pre[0]]
        
        WHITE = 1
        GRAY = 2
        BLACK = 3
        all_nodes = {i: WHITE for i in range(numCourses)}
        
        no_cycle = True
        def dfs(node):
            nonlocal no_cycle
            if not no_cycle:
                return
            
            all_nodes[node] = GRAY

            if node in courses:
                for neighbor in courses[node]:
                    if all_nodes[neighbor] == WHITE:
                        dfs(neighbor)
                    elif all_nodes[neighbor] == GRAY:
                        no_cycle = False
            
            all_nodes[node] = BLACK
            
        for key in courses:
            dfs(key)
        
        return no_cycle