/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    trueHead := head
    for head != nil && head.Next != nil {
        if head.Next.Val == val {
            head.Next = head.Next.Next
        } else {
            head = head.Next
        }
    }
    
    if trueHead != nil && trueHead.Val == val {
        return trueHead.Next
    }
    
    return trueHead
}