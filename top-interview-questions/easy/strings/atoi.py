#### https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        sign = False
        negative = False
        first = False
        number = 0

        for c in str:
            if c == "-" and sign == False and negative == False and first == False:
                sign = True
                negative = True
            elif c == "+" and sign == False and negative == False and first == False:
                sign = True
                negative = False
            elif c.isdigit() == False:
                break
            else:
                if first == False:
                    first = True
                number *= 10
                number += int(c)

        print(number)

        if negative:
            if -1 * number < -1 * (2**31):
                return (-1 * (2**31))
            else:
                return number * -1
        else:
            if number > 2**31 - 1:
                return 2**31 - 1
            else:
                return number
