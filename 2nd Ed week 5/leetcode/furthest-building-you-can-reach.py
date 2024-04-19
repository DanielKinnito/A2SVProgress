class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        move = 1

        while move < len(heights):
            step = heights[move] - heights[move - 1]

            if step > 0:
                heappush(heap, step)

                if len(heap) > ladders:
                    bricks -= heappop(heap)
                
                if bricks < 0:
                    return move - 1
            
            move += 1
        
        return move - 1