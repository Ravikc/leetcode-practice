/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return false
    }
    
    fast := head.Next.Next
    slow := head
    
    for {
        if fast == slow {
            return true
        }
        
        if fast == nil || fast.Next == nil {
            return false
        }
        
        fast = fast.Next.Next
        slow = slow.Next
    }
}