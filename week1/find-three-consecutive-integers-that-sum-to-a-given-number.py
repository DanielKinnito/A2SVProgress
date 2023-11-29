class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        answer = []
        if num % 3 != 0:
            answer = []
            return answer
        check = num//3
        
        return check-1,check,check+1