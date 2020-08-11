#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(0, len(nums)):
            if(nums[i] != 0):
                nums[index] = nums[i]
                index = index + 1

        for i in range(index, len(nums)):
            nums[i] = 0
