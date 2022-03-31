# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head;
        
        one = None
        two = head
        three = head.next
        head = three
        index = 2
        
        while three != None:
            if index % 2 == 0:
                if one != None:
                    one.next = three
                
                two.next = three.next
                three.next = two
                one = three
                three = two.next
            else:
                one = two
                two = three                
                three = three.next
                
            index += 1
                
        
        
        return head
        