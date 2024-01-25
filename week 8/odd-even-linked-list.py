# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head = ListNode(-1)
        even_head = ListNode(-1)

        odd_tail = odd_head
        even_tail = even_head

        is_odd = True
        current = head
        while current:
            if is_odd:
                odd_tail.next = current
                odd_tail = odd_tail.next

            else:
                even_tail.next = current
                even_tail = even_tail.next

            is_odd = not is_odd
            current = current.next

        odd_tail.next = even_head.next
        even_tail.next = None
        
        return odd_head.next