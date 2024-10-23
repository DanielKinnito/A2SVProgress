class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        
        MOD = 10**9 + 7
        base = 26 + 1
        length = len(needle)

        def convert(char):
            return ord(char) - 96

        def addLast(Hash, letter):
            return (Hash * base + convert(letter)) % MOD
        
        def pollFirst(Hash, letter, power):
            return (Hash - convert(letter) * power) % MOD
        
        powers = [1] * (length + 1)

        for i in range(1, length + 1):
            powers[i] = powers[i-1] * base % MOD

        needle_hash = 0
        hay_hash = 0
        for i in range(length):
            needle_hash = addLast(needle_hash, needle[i])
            hay_hash = addLast(hay_hash, haystack[i])

        for i in range(len(haystack) - length + 1):
            if needle_hash == hay_hash:
                if haystack[i:i + length] == needle:
                    return i
            if i + length < len(haystack):
                hay_hash = pollFirst(hay_hash, haystack[i], powers[length - 1])
                hay_hash = addLast(hay_hash, haystack[i + length])

        return -1