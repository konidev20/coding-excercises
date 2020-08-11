#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        multiplier = 10 ** (size-1)
        number = 0
        for digit in digits:
            number += digit * multiplier
            multiplier = multiplier // 10

        number = number + 1

        temp = list()
        while number > 0:
            temp.append((number % 10))
            number = number // 10
        temp.reverse()

        digits = temp.copy()

        return digits
