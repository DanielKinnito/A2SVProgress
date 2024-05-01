class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        
        def find_ones(num):
            if num == 0:
                return 0
            return find_ones(num >> 1) + (num & 1)

        return find_ones(temp)