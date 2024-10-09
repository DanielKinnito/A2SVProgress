class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = {node: inf for node in range(1, n+1)}
        distances[k] = 0

        processed = set()

        heap = [(0, k)]
        while heap:
            cur_dist, cur_node = heappop(heap)
            if cur_node in processed:
                continue
            processed.add(cur_node)

            for node, weight in graph[cur_node]:
                dist = cur_dist + weight
                if dist < distances[node]:
                    distances[node] = dist
                    heappush(heap, (distances[node], node))
        
        min_time = max(distances.values())

        return min_time if min_time != inf else -1