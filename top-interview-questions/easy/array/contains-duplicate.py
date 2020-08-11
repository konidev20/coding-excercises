#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        index = {}
        for number in nums:
            if number not in index:
                index[number] = 1
            else:
                return True
        return False
