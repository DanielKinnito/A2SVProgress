# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sorted_head = ListNode(float('-inf'))
        curr = head

        while curr:
            # Sever the node
            temp = curr
            curr = curr.next
            temp.next = None

            prev = None
            current_sorted = sorted_head # a ptr to iterate through the list

            while current_sorted and temp.val > current_sorted.val:
                prev = current_sorted
                current_sorted = current_sorted.next

            # if it's supposed to be at the first postion
            if not prev:
                temp.next = sorted_head
                sorted_head = temp
            # if we found a place for it
            else:
                prev.next = temp
                temp.next = current_sorted

        return sorted_head.next