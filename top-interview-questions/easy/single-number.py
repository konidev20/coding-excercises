#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = {}
        for num in nums:
            if num not in index:
                index[num] = 0
            index[num] += 1

        for num in nums:
            if index[num] != 2:
                return num
