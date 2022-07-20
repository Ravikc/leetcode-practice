func getMiddle(node *ListNode) *ListNode {    
    slow := node
    fast := node
    prevSlow := node
    
    for {
        if fast == nil || fast.Next == nil {
            prevSlow.Next = nil
            return slow
        }
        
        fast = fast.Next.Next
        prevSlow = slow
        slow = slow.Next
        
    }
}

func reverse(node *ListNode) *ListNode {
    next := node.Next
    node.Next = nil
    for next != nil {
        tempNext := next
        next = tempNext.Next
        tempNext.Next = node
        node = tempNext
    }
    
    return node
}

func isPalindrome(head *ListNode) bool {
    mid := getMiddle(head)
    last := reverse(mid)
    
    left := head
    right := last
    
    for left != nil && right != nil {
        if left.Val != right.Val {
            return false
        }
        
        left = left.Next
        right = right.Next        
    }
    
    return true
}