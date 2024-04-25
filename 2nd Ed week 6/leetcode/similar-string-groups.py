class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        root = {s: s for s in strs}
        size = {s: 1 for s in strs}
        answer = len(root)
        
        def checker(s, c):
            count, length = 0, len(s)

            for i in range(len(s)):
                if s[i] == c[i]: count += 1
            
            return count >= length - 2
        
        def find(x):
            if root[x] != x:
                root[x]= find(root[x])
            return root[x]
          
        def union(x, y):
            rx = find(x)
            ry = find(y)

            if rx != ry:
                if size[rx] > size[ry]:
                    root[ry] = rx
                    size[rx] += size[ry]
                else:
                    root[rx] = ry
                    size[ry] += size[rx]
                # root[rx] = ry
                
                # if rank[rx] == rank[ry]:
                #     root[ry] = rx
                # elif rank[rx] < rank[ry]:
                #     root[rx] = ry
                #     rank[ry] += 1
                # else:
                #     root[ry] = rx
                #     rank[rx] += 1

        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                string, check = strs[i], strs[j]
                if checker(string, check) and find(string) != find(check):
                    union(string, check)
                    answer -= 1
        
        return answer