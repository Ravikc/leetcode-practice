class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        newStack = []
        curr = head
        
        while curr:
            if curr.child:
                stack.append(curr);
                newStack.append(curr.child)
                curr = curr.child
                continue
            
            if curr.next:
                curr = curr.next
                continue
            
            if len(stack) > 0:
                oldCurr = stack.pop()
                oldCurr.child = None
                newHead = newStack.pop()
                oldNext = oldCurr.next #if oldCurr.next else stack[-1]
                
                oldCurr.next = newHead
                newHead.prev = oldCurr
                
                if oldNext:
                    curr.next = oldNext
                    oldNext.prev = curr
                    
                curr = oldCurr
                continue
              
            curr = curr.next
            
        return head
                
                
            
        