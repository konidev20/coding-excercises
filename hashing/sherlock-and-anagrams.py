#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    substrings = [(s[i:j],list(range(i,j))) for i in range(len(s)) for j in range (i+1,len(s)+1) if s[i:j] != s]
    count = 0
    anagrams = {}
    for i in range(len(substrings)):
        a, x = substrings[i]
        a = sorted([c for c in a])
        hashed = hash(str(a))
        if str(a) not in anagrams:
            anagrams[str(a)] = 0
        anagrams[str(a)] += 1
    count = sum([(x*(x-1)//2) for x in list(anagrams.values())])
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
