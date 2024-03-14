# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = [[] for _ in range(k)]
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        part_len = length // k
        remain = length % k

        prev = None
        for i in range(k):
            answer[i] = head
            
            for j in range(part_len + (1 if remain > 0 else 0)):
                prev = head
                head = head.next
            
            if prev:
                prev.next = None
            
            remain -= 1

        return answer