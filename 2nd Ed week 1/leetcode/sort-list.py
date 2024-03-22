# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        def merge(left_half, right_half):
            dummy = ListNode(0)
            temp_head = dummy

            while left_half and right_half:
                if right_half.val > left_half.val:
                    temp_head.next = left_half
                    left_half = left_half.next
                
                else:
                    temp_head.next = right_half
                    right_half = right_half.next
                
                temp_head = temp_head.next
            
            if left_half:
                temp_head.next = left_half
            
            if right_half:
                temp_head.next = right_half
            
            return dummy.next
        
        if not head or not head.next:
            return head
        left = head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow
        right = middle.next
        middle.next = None

        left = self.sortList(left)
        right = self.sortList(right)
        
        return merge(left, right)