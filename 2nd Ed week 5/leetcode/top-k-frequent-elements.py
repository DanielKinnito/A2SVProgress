class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        
        for num in count:
            heappush(heap, (count[num], num))
            if len(heap) > k:
                heappop(heap)
        answer = []
        
        for iterable in heap:
            answer.append(iterable[1])

        return answer