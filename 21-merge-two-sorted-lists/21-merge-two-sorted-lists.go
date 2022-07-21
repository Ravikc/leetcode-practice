/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    var head *ListNode
    runner := &ListNode{}
    
    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            runner.Next = list1
            list1 = list1.Next
        } else {
            runner.Next = list2
            list2 = list2.Next
        }
        
        runner = runner.Next
        if head == nil {
            head = runner
        }
    }
    
    for list1 != nil {
        runner.Next = list1
        list1 = list1.Next
        runner = runner.Next
        if head == nil {
            head = runner
        }
    }
    
    for list2 != nil {
        runner.Next = list2
        list2 = list2.Next
        runner = runner.Next
        if head == nil {
            head = runner
        }
    }
    
    return head
}