class Solution:
    def findComplement(self, num: int) -> int:
        length = num.bit_length()
        compare = '1' * length
        return num ^ int(compare, 2)