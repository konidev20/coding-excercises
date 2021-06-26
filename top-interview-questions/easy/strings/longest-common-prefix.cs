//https://leetcode.com/problems/longest-common-prefix
public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        if (strs.Length == 0) return "";
        if (strs.Length == 1) return strs[0];

        var lcp = LCP(strs[0], strs[1]);

        if (string.Equals(lcp, "")) return "";

        for (int i = 2; i < strs.Length; i++)
        {
            lcp = LCP(lcp, strs[i]);
            if (string.Equals(lcp, "")) return "";
        }
        return lcp;
    }

    public string LCP(string str1, string str2)
    {
        if (string.Equals(str1, "")) return "";

        if (string.Equals(str1, str2)) return str1;

        int compareLength = Math.Min(str1.Length, str2.Length);

        StringBuilder stri = new StringBuilder("");

        for (int i = 0; i < compareLength; i++)
        {
            if (str1[i] == str2[i])
            {
                stri.Append(str1[i]);
            }
            else
            {
                break;
            }
        }
        return stri.ToString();
    }
}