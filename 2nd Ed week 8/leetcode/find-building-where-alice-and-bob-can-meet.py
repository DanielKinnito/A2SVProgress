class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1] * len(queries)
        temp = []
        
        for i, query in enumerate(queries):
            a, b = sorted(query)
            if a == b or heights[b] > heights[a]:
                answer[i] = b
            else:
                temp.append((i, a, b))
        
        temp.sort(key = lambda x: x[2], reverse = True)
        mono = deque()
        index = len(heights) - 1
        
        for i, a, b in temp:
            while index > b:
                while mono and heights[index] >= heights[mono[0]]:
                    mono.popleft()
                mono.appendleft(index)
                index -= 1
            
            loc = -1
            l, r = 0, len(mono) - 1
            
            while l <= r:
                p = (l + r) // 2
                if heights[mono[p]] > heights[a]:
                    loc = mono[p]
                    r = p - 1
                else:
                    l = p + 1
            
            answer[i] = loc
        
        return answer