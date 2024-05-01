class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        length = n.bit_length()
        compare = '1' * length
        return n ^ int(compare, 2)