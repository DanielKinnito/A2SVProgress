class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = {i: [0, 0] for i in range(1, n+1)}
        for pair in trust:
            trusted[pair[1]][0] += 1
            trusted[pair[0]][1] += 1

        for key in trusted:
            if trusted[key][0] == n - 1 and trusted[key][1] == 0:
                return key
        
        return -1