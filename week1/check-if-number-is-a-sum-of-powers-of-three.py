class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ternary = []
        while n > 0:# to store the ternary values
            ternary.append(n % 3)
            n //= 3
        #check if there are other numbers other than 0 and 1
        for digit in ternary: 
            if digit not in {0, 1}:
                return False
        return True        