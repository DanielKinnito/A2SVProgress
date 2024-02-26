from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
            1. make queues for both and store indices as they are from the senate
            2. pop elements from the begining and compare the indices
                2.1. deque from the largest index and append the other with + n to ensure that it is at the last
            3. return the queue that is not empty
        """
        dire_que = deque()
        radiant_que = deque()
        length = len(senate)

        for i in range(length):
            if senate[i] == 'R':
                radiant_que.append(i)
            else:
                dire_que.append(i)
        
        while dire_que and radiant_que:
            dire_turn = dire_que.popleft()
            radiant_turn = radiant_que.popleft()
            
            if dire_turn < radiant_turn:
                dire_que.append(dire_turn + length)
            else:
                radiant_que.append(radiant_turn + length)
        
        return 'Radiant' if radiant_que else 'Dire'