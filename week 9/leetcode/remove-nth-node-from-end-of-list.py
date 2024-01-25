# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        slow = head
        fast = head

        for _ in range(n):# move until fast is n length far from slow
            if not fast:
                return head
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:#move both until fast is at the end
            slow = slow.next
            fast = fast.next

        if slow.next:#delete the node at slow
            slow.next = slow.next.next

        return head