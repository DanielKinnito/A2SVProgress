# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        less_head = ListNode(-1)
        more_head = ListNode(-1)

        less_tail = less_head
        more_tail = more_head

        is_less = True
        current = head
        while current:
            if current.val < x:
                is_less = True
            else:
                is_less = False

            if is_less:
                less_tail.next = current
                less_tail = less_tail.next

            else:
                more_tail.next = current
                more_tail = more_tail.next

            is_less = not is_less
            current = current.next

        less_tail.next = more_head.next
        more_tail.next = None
        
        return less_head.next