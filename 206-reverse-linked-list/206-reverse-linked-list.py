class Solution:
    def reverse(self, prev, node):
        if not  node:
            return prev
        
        temp = node.next
        node.next = prev
        return self.reverse(node, temp)
    
    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(None, node)