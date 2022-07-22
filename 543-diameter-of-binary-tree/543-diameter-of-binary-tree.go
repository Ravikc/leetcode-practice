/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var ans int

func max(a, b int) int {
    if a > b {
        return a
    }
    
    return b
}

func diameter(root *TreeNode) int {
    if root == nil {
        return 0
    }    
    
    left := diameter(root.Left)
    right := diameter(root.Right)
    
    ans = max(ans, left + right)
    return max(left, right) + 1
}

func diameterOfBinaryTree(root *TreeNode) int {
    ans = 0
    diameter(root)
    return ans
}