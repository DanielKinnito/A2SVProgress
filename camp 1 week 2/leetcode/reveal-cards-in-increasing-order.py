from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        queue = deque()
        
        for num in deck:
            if queue:
                popped = queue.pop()
                queue.appendleft(popped)
                queue.appendleft(num)
            else:
                queue.append(num)

        answer = []
        for num in queue:
            answer.append(num)
            
        return answer