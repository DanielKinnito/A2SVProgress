class Solution:
    def isHappy(self, n: int) -> bool:
        """
        1 - make a set
        2 - use the set to keep track of seen numbers and detect cycles
        3 - convert the numbers to str and sum each sqr as int to another var
        4 - return true or false based on whether answer == 1
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1