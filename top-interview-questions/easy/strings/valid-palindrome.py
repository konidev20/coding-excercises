#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if len(s) == 0:
            return True

        clean = ""
        for c in s:
            if c.isalnum():
                clean += c

        if clean[::-1] == clean:
            return True

        return False
