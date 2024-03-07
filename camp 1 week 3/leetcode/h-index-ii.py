class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        def noIndices(mid):
            cur_index = bisect_right(citations, mid)
            cur_length = length - cur_index

            if cur_length > mid:
                return True
            return False
        
        left = 0
        right = length

        while left <= right:
            middle = (left + right) // 2

            if noIndices(middle):
                left = middle + 1
            else:
                right = middle - 1
        
        return left