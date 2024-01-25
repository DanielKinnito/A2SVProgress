# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_start = dummy

        for _ in range(left - 1):
            prev_start = prev_start.next

        prev = None
        curr = prev_start.next
        diff = right - left + 1

        while diff > 0:#flip
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            diff -= 1

        prev_start.next.next = curr
        prev_start.next = prev

        return dummy.next