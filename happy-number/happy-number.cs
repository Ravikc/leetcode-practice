public class Solution {
    public bool IsHappy(int n) {
        int slow = n;
        int fast = GetNext(n);
        
        while (true)
        {
            slow = GetNext(slow);
            fast = GetNext(GetNext(fast));
            
            if (fast == 1) return true;
            if (slow == fast) return false;            
        }
        
        return false;
    }
    
    private int GetNext(int n)
    {
        int num = 0;
        while (n > 0)
        {
            int last = n % 10;
            num += (last * last);
            n = n / 10;
        }
        
        return num;
    }    
   
}