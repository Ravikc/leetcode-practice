public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        var dic = new Dictionary<char, int>();
        
        foreach (char c in s)
        {
            if (!dic.ContainsKey(c)) dic.Add(c, 0);
            dic[c] += 1;
        }
        
        foreach (char c in t)
        {
            if (!dic.ContainsKey(c)) return false;
            dic[c] -= 1;
        }
        
        return dic.Values.All(x => x == 0);
    }
}