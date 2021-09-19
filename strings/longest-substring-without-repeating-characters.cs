//https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

public class Solution {
    public int LengthOfLongestSubstring(string s) 
    {   
        Dictionary<char, int> map = new Dictionary<char, int>();
        
        int longest = 0;
        
        int start = 0;
        
        for(int end = 0; end < s.Length; end++){
            int length = 0;
            if(map.TryGetValue(s[end], out int val)){
                start = Math.Max(start, val + 1);
            }
            
            map[s[end]] = end;
            longest = Math.Max(longest, end-start + 1);
        }
        return longest;
    }
}