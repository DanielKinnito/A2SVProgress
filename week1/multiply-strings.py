class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        result = [0] * (m + n)
        for i in range(m - 1,-1,-1):
            carry = 0
            for j in range(n - 1,-1,-1):
                temp = (int(num1[i])) * (int(num2[j])) + carry + result[i + j + 1]
                result[i + j + 1] = temp % 10
                carry = temp // 10

            result[i] += carry
        answer = "".join(map(str, result))
        answer = answer.lstrip("0")
        if not answer:
            return "0" 
        else:
            return answer
