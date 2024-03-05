class Solution:
    def numberOfWays(self, s: str) -> int:
        """
            1. Maintain a dynamic count of valid selections
            -by considering the types of the last two buildings
            2. Accumulate the total count of valid selections, 
            - avoid two consecutive buildings of the same type
        """
        
        n = len(s)
        answer = 0

        seen = [[0] * 2 for _ in range(2)]

        for i in range(n):
            current = int(s[i])

            answer += seen[1][1- current]
            seen[1][current] += seen[0][1 - current]
            seen[0][current] += 1
        
        return answer