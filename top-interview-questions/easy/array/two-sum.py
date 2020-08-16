#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, number in enumerate(nums):
            if number in seen and seen[number] != index:
                i = seen[number]
                j = index
                return [i, j]
            else:
                seen[target-number] = index
