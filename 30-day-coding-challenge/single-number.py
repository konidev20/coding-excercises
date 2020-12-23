# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        
        for number in nums:
            if number not in count:
                count[number] = 0
            count[number] += 1
            
        for n,c in count.items():
            if c != 2:
                return n