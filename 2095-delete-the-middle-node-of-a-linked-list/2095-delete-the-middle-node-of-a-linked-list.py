# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMidAndPrev(self, head):
        slow = fast = head
        slower = None
        while fast and fast.next:
            fast = fast.next.next
            slower = slow
            slow = slow.next
            
        return (slower, slow)
    
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, mid = self.getMidAndPrev(head)
        if not prev:
            return None
        
        prev.next = mid.next
        mid.next = None
        return head