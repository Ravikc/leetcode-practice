class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        one = None
        two = three = head
        
        for i in range(n - 1):
            three = three.next
            
        while three.next:
            one = two
            two = two.next
            three = three.next
        
        if two == head:
            return two.next
        
        if one:
            one.next = two.next
        else:
            two.next
            
        two.next = None
        return head
        