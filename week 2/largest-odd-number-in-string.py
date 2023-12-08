class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        answer = ""

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                answer += num[:i+1]
                break
        return answer