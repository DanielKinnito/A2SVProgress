class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        queue = deque((idx, ticket) for idx,ticket in enumerate(tickets))
        ticket_dict = {idx: ticket for idx, ticket in enumerate(tickets)}
        
        while queue:
            cur_ticket = queue.popleft()
            ticket_dict[cur_ticket[0]] -= 1
            count += 1
            
            if cur_ticket[1] > 1:
                queue.append((cur_ticket[0], cur_ticket[1] - 1))
            
            if ticket_dict[k] == 0:
                return count