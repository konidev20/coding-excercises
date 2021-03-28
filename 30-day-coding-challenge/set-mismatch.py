### https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dict = {i:0 for i in range(1,n+1)}
        
        repeated = 0
        
        for num in nums:
            dict[num] += 1
            if dict[num] > 1:
                repeated = num
        
        missing = list(dict.keys())[list(dict.values()).index(0)]
        
        return [repeated,missing]