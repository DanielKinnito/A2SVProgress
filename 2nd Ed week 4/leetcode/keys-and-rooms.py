class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for i, room in enumerate(rooms):
            adj_list[i] = room
        
        que = deque()
        visited = set()
        que.append(0)

        while que:
            node = que.popleft()
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    que.append(neighbor)
        
        return len(rooms) == len(visited)