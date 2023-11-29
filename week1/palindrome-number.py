class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrome = str(x)        
        return palindrome == palindrome[::-1]