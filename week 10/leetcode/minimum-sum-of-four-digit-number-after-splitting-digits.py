class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        string = []
        for c in s:
            string.append(int(c))
        
        string.sort()
        temp1 = str(string[0]) + str(string[2])
        temp2 = str(string[1]) + str(string[3])

        return int(temp1) + int(temp2)