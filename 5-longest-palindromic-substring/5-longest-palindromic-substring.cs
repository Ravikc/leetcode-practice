public class Solution {
    public string LongestPalindrome(string s) 
    {
        bool[,] arr = new bool[s.Length, s.Length];
        string longest = "";
        int wordLen = 1;
        while (wordLen <= s.Length)
        {
            for (int i = 0; i <= s.Length - wordLen; i++)
            {
                if (wordLen == 1)
                {
                    longest = s[i].ToString();
                    arr[i, i] = true;
                }
                else if (wordLen == 2 && s[i] == s[i + 1])
                {
                    arr[i, i + 1] = true;
                    longest = s.Substring(i, wordLen);
                }
                else if (s[i] == s[i + wordLen - 1] && arr[i + 1, i + wordLen - 2])
                {
                    arr[i, i + wordLen - 1] = true;
                    longest = s.Substring(i, wordLen);
                }
            }
            
            wordLen++;
        }
        
        return longest;
    }
}