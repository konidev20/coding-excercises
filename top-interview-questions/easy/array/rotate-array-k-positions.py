#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
class Solution(object):
    def reverse(self, low, high, nums):
        l = low
        h = high
        while(l < h):
            temp = nums[l]
            nums[l] = nums[h]
            nums[h] = temp
            l += 1
            h -= 1
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x = k % len(nums)
        self.reverse(0,len(nums)-1,nums)
        self.reverse(0,x-1,nums)
        self.reverse(x,len(nums)-1,nums)
