# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_a = headA
        list_b = headB

        while list_a != list_b:
            if list_a:
                list_a = list_a.next
            else:
                list_a = headB
            
            if list_b:
                list_b = list_b.next
            else:
                list_b = headA
        
        return list_a