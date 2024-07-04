class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        for key in adj_list:
            if len(adj_list[key]) > 1:
                return key