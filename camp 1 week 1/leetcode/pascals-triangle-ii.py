class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: # Best case 1
            return [1]
        elif rowIndex == 1: # Best case 2
            return [1,1]
        else:
            prev = self.getRow(rowIndex - 1) # Recursion relation
            curr = [1]
            for i in range(1, rowIndex):
                curr.append(prev[i - 1] + prev[i])
            curr.append(1)

            return curr