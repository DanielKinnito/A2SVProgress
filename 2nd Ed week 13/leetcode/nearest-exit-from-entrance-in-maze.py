class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        width = len(maze[0])
        height = len(maze)
        
        def isborder(x, y):
            return (x == 0 or x == height-1 or y == 0 or y == width-1) and [x, y] != entrance
        
        def inbound(x, y):
            return (0 <= x < height) and (0 <= y < width)

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        visited = set()
        que = deque()

        que.append((entrance[0], entrance[1]))
        visited.add((entrance[0], entrance[1]))
        steps = 0

        while que:
            size = len(que)
            for _ in range(size):
                x, y = que.popleft()
                
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    coord = (new_x, new_y)

                    if inbound(new_x, new_y) and (new_x, new_y) not in visited and maze[new_x][new_y] == '.':

                        if isborder(new_x, new_y):
                            return steps + 1
                        
                        que.append(coord)
                        visited.add(coord)
            steps += 1  
        
        return -1