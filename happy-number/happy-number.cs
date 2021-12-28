public class Solution {
    public bool IsHappy(int n) {
        var set = new HashSet<int>();
        return IsHappy(n, set);
    }
    
    private bool IsHappy(int n, HashSet<int> set)
    {
        int num = 0;
        while (n > 0)
        {
            int last = n % 10;
            num += (last * last);
            n = n / 10;
        }
        
        if (num == 1) return true;
        
        if (set.Contains(num)) return false;
        
        set.Add(num);
        return IsHappy(num, set);
    }
}