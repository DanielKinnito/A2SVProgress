class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        # Recursive call
        answer = self.generate(numRows - 1)
        

        prev = answer[-1]
        curr = [1]
        for i in range(1, len(prev)):
            curr.append(prev[i-1] + prev[i])
        curr.append(1)
        
        answer.append(curr)
        return answer