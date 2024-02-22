from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # count = 0
        # answer = 0
        # queue = deque(tickets)

        # while tickets[k] != 0:
        #     cur_ticket = queue.popleft()
        #     count += 1
        #     cur_ticket -= 1
        #     if cur_ticket > 0:
        #         queue.append(cur_ticket)
        #         k = (k + 1) % len(queue)
        #     if k != 0 and count % k == 0:
        #         tickets[k] -= 1
        #         answer += len(queue)

        # return answer
        answer = 0
        n = len(tickets)
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i]:
                    tickets[i] -= 1
                    answer += 1

                    if tickets[k] == 0:
                        return answer