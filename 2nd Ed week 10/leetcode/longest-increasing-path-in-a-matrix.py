class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        def inbound(x, y):
            return 0 <= x < n and 0 <= y < m

        directions = [
            [1, 0], [-1, 0],
            [0, 1], [0, -1]
        ]

        indegree = {}
        directed = defaultdict(list)
        for i in range(n):
            for j in range(m):
                for x, y in directions:
                    if inbound(i + x, j + y) and matrix[i+x][j+y] > matrix[i][j]:
                        directed[(i, j)].append((i+x, j+y))
                        indegree[(i+x, j+y)] = indegree.get((i+x, j+y), 0) + 1 
        
        que = deque()
        for i in range(n):
            for j in range(m):
                if (i, j) not in indegree:
                    que.append((i, j))
        
        level = 0
        while que:
            size = len(que)
            for _ in range(size):
                coord = que.popleft()
                for neighbor in directed[coord]:
                    if neighbor in indegree:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            del indegree[neighbor]
                    if neighbor not in indegree:
                        que.append(neighbor)

            level += 1
        # print(directed)
        # print('\n', indegree)
        return level
