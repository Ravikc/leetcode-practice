
public class Solution {
    public bool IsSubtree(TreeNode root, TreeNode subRoot)
    {
        if (root == null) return false;
        if (Same(root, subRoot)) return true;
        
       return IsSubtree(root?.left, subRoot)
           || IsSubtree(root?.right, subRoot);
    }
    
    public bool Same(TreeNode n1, TreeNode n2)
    {
        Console.WriteLine($"Comparing {n1?.val} and {n2?.val}");
        
        if (n1 == null && n2 == null) return true;
        if (n1 == null || n2 == null) return false;
        
        if (n1.val != n2.val) return false;
        
        return Same(n1.left, n2.left) && Same(n1.right, n2.right);
    }
    
    
}