class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        string = list(map(lambda x: dictionary[x], s))
        answer = 0
        
        for i in range(len(string)):
            if i < len(string) - 1 and string[i] < string[i + 1]:
                answer -= string[i]
            else:
                answer += string[i]
        return answer