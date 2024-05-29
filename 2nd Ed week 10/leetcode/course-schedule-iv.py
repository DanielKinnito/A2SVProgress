class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0] * numCourses

        directed = defaultdict(list)
        for u, v in prerequisites:
            directed[u].append(v)
            indegree[v] += 1

        que = deque()
        reachable = defaultdict(set)

        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        
        while que:
            node = que.popleft()
            for ne in directed[node]:
                reachable[ne].add(node)
                reachable[ne].update(reachable[node])
                
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    que.append(ne)
        
        answer = []
        for x, y in queries:
            if x in reachable[y]:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer