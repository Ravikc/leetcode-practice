# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        for i in range(k - 1):
            fast = fast.next
            
        one = fast
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            
        temp = slow.val
        slow.val = one.val
        one.val = temp
        
        return head