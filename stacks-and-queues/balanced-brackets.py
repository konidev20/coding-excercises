#!/bin/python3

#https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    opening = ["(","[","{"]
    closing = ["}","]",")"]
    pairs = [("(",")"),("[","]"),("{","}")]
    
    for bracket in s:
        if bracket in opening:
            stack.append(bracket)
        if bracket in closing:
            if len(stack) == 0:
                stack.append(bracket)
                continue
            top = len(stack) - 1;
            if (stack[top],bracket) in pairs:
                stack.pop()
            else:
                stack.append(bracket)

    if len(stack) == 0:
        return "YES"
                
    return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
