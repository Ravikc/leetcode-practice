/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    runner := head
    for runner != nil && runner.Next != nil {
        if runner.Val == runner.Next.Val {
            runner.Next = runner.Next.Next
        } else {
            runner = runner.Next
        }
    }
    
    return head
}