/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    slow := head
    fast := head
    
    for {
        if fast == nil || fast.Next == nil {
            return slow
        }
        
        slow = slow.Next
        fast = fast.Next.Next    
    }
}