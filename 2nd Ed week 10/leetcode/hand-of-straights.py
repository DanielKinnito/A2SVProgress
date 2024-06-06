class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        if length % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        
        while min_heap:
            first = min_heap[0]
            
            for i in range(groupSize):
                current = first + i
                
                if count[current] == 0:
                    return False
                count[current] -= 1
                
                if count[current] == 0:
                    if current != min_heap[0]:
                        return False
                    
                    heapq.heappop(min_heap)
        
        return True