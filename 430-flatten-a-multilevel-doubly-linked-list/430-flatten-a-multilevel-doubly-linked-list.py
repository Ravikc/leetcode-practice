class Solution:
    def flatten(self, node: 'Optional[Node]') -> 'Optional[Node]':
        orig = node
        if not node:
            return 
        
        
        if node.child:
            newLL = self.flatten(node.child)
            temp = node.next
            node.next = newLL
            newLL.prev = node
            node.child = None
            while newLL.next:
                newLL = newLL.next
                
            newLL.next = temp
            if temp:
                temp.prev = newLL
                
            node = newLL.next
         
        if node:
            self.flatten(node.next)
        return orig
                
                
            
        