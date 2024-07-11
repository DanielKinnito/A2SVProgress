class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        
        cur = answer
        temp = 0
        head = head.next
        
        while head:
            if head.val == 0:
                cur.next = ListNode(temp)
                cur = cur.next
                temp = 0
            
            else:
                temp += head.val
            
            head = head.next
        
        return answer.next