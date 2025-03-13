class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for num in nums:
            num = int(num)
            
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        
        return str(heap[0])