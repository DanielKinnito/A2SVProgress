# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow
        

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare the two halves
        ptr_one = head
        ptr_two = prev

        while ptr_two:
            if ptr_one.val != ptr_two.val:
                return False
            ptr_two = ptr_two.next
            ptr_one = ptr_one.next

        return True
