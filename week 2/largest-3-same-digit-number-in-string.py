class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        answer = ""

        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if sub.count(sub[0]) == 3:
                if sub > answer:
                    answer = sub
        return answer        