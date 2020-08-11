#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = {}
        for c in s:
            if c not in index:
                index[c] = 0
            index[c] += 1

        for i, c in enumerate(s):
            if index[c] == 1:
                return i

        return -1
