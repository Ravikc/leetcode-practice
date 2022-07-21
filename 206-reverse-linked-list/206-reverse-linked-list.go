/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    
    one, two, three := head, head.Next, head.Next.Next    
    one.Next = nil
    
    for two != nil {
        two.Next = one
        one = two
        two = three
        
        if three != nil {
            three = three.Next                
        }
    }
    
    return one
}