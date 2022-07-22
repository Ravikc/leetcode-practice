/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */
func find(root, p, q *TreeNode) *TreeNode {
    if p.Val <= root.Val && root.Val <= q.Val {
        return root
    }
    
    if p.Val <= root.Val && q.Val <= root.Val {
        return lowestCommonAncestor(root.Left, p, q)
    }
    
    return lowestCommonAncestor(root.Right, p, q)
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    if p.Val > q.Val {
        p, q = q, p
    }
    
    return find(root, p, q)
}