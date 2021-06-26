//https://leetcode.com/problems/palindrome-number

using System;
using System.Generics;

public class Solution {
    public bool IsPalindrome(int x) {
        if(x < 0) return false;
        
        var digitCounter = 0;
        var copy = x;
        var reverse = 0;
        var digits = new Stack<int>();
        
        while(copy > 0){
            var digit = copy % 10;
            reverse = reverse * 10 + digit;
            copy /= 10;
        }
        
        if(reverse != x){
            return false;
        }
        return true;
    }
}