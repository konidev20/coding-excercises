## https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3669/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n_unique = pow(2,k)
        
        substrings = [s[i:i+k] for i in range(len(s)-k+1)]
        
        unique = {}
        
        for substring in substrings:
            if substring not in unique:
                unique[substring] = 0
            unique[substring] += 1
            
        if len(list(unique.keys())) == n_unique:
            return True
        
        return False