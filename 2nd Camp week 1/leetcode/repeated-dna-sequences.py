class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()
        
        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
        
        return list(repeated)