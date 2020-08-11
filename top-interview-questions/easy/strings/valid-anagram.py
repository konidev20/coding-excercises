#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}
        for c in s:
            if c not in dict:
                dict[c] = 0
            dict[c] += 1

        for c in t:
            if c not in dict:
                return False
            else:
                dict[c] -= 1

        for k, v in dict.items():
            if v > 0:
                return False

        return True
