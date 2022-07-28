public class Solution {
    public bool BackspaceCompare(string s, string t) {
        int one = s.Length - 1;
        int two = t.Length - 1;
        
        while (one >= 0 || two >= 0)
        {
            int back = 0;
            while (one >= 0 && (s[one] == '#' || back > 0))
            {
                if (s[one] == '#')
                {
                    back += 1;
                    one -= 1;
                }
                else
                {
                    back -= 1;
                    one -= 1;
                }
            }
            
            back = 0;
            while (two >= 0 && (t[two] == '#' || back > 0))
            {
                if (t[two] == '#')
                {
                    back += 1;
                    two -= 1;
                }
                else
                {
                    back -= 1;
                    two -= 1;
                }
            }
            
            if (one < 0 && two < 0)
            {
                return true;
            }
            if (one < 0 || two < 0)
            {
                return false;
            }
            
            if (s[one] != t[two])
            {
                return false;
            }
            
            one -= 1;
            two -= 1;                
        }
        
        return one == -1 && two == -1;
    }
}