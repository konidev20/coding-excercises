#### https://leetcode.com/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x: int) -> int:
        number = abs(x)
        sign = 1
        if x < 0:
            sign = -1

        reverse = 0

        while number > 0:
            reverse = reverse * 10
            reverse += (number % 10)
            number = number // 10

        if (reverse*sign) > (2**31-1) or (reverse*sign) < (-2**31):
            return 0

        return reverse * sign
