# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]: 
                num = lists[i].val
                heappush(heap, (num, i, lists[i]))
        
        answer = ListNode(0)
        curr = answer

        while heap:
            num, idx, node = heappop(heap)
            
            dummy = ListNode(num)
            curr.next = dummy
            curr = curr.next
            
            if node.next: 
                num = node.next.val
                heappush(heap, (num, idx, node.next))
            
        return answer.next