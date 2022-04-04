# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        left = head
        right = head
        
        while right != None:
            size += 1
            if size == k:
                left = right
                
            right = right.next
            
        right = head
        i = 0
        while i < size - k:
            right = right.next
            i += 1
            
        temp = left.val
        left.val = right.val
        right.val = temp
            
        print(size)
        return head