#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s)-1

        while low < high:
            temp = s[low]
            s[low] = s[high]
            s[high] = temp
            low = low+1
            high = high-1
