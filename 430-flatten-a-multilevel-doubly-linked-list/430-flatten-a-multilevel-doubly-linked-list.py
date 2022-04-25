class Solution:
    def flatten(self, node: 'Optional[Node]') -> 'Optional[Node]':
        self.flattenHelper(node)
        return node
        
    def flattenHelper(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:
            return node
        
        if not node.next and not node.child:
            return node        
        
        if node.child:
            newLL = self.flattenHelper(node.child)
            temp = node.next
            node.next = node.child
            node.child.prev = node
            node.child = None
            
            newLL.next = temp
            if temp:
                temp.prev = newLL
                
            node = newLL.prev
             
            
        if node:
            return self.flattenHelper(node.next)
        
        return node
