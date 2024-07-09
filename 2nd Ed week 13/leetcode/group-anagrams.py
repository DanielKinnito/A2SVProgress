class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            temp = ''.join(sorted(word))
            groups[temp].append(word)
            
        return list(groups.values())