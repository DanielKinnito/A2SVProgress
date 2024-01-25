# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        intersection = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                intersection = slow
                break
        
        if not intersection:
            return intersection

        ptr = head
        while ptr != intersection:
            ptr = ptr.next
            intersection = intersection.next
        
        return intersection