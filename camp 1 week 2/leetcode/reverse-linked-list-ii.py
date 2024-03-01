# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        prev_start = None
        curr = head
        for _ in range(left - 1):
            prev_start = curr
            curr = curr.next

        prev = None
        start = curr
        diff = right - left + 1

        while diff > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            diff -= 1

        if prev_start:
            prev_start.next = prev
        else:
            head = prev

        start.next = curr

        return head