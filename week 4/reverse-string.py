class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        front = 0
        back = n-1
        
        while front < n/2 :
            s[front], s[back] = s[back], s[front]

            front += 1
            back -= 1