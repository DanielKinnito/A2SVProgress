class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = set(nums)

        heap = []
        for num in distinct:
            heappush(heap, num)
            if len(heap) > 3:
                heappop(heap)
        
        if len(heap) < 3:
            return max(distinct)
        else:
            return heap[0]
            