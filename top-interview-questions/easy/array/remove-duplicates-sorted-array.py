##### https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1, len(nums)):
            current = nums[index]
            if(nums[i] != current):
                index = index + 1
                nums[index] = nums[i]
        return index + 1
