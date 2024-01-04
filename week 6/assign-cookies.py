class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0
        left, right = 0, 0

        while left < len(g) and right < len(s):
            if s[right] >= g[left]:
                content_children += 1
                left += 1
                
            right += 1

        return content_children