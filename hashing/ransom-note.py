## https://www.hackerrank.com/challenges/ctci-ransom-note/problem 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    flag = True
    
    magDict = {}
    
    for word in magazine:
        if word not in magDict:
            magDict[word] = 0
        magDict[word] += 1
    
    notDict = {}
    
    for word in note:
        if word not in notDict:
            notDict[word] = 0
        notDict[word] += 1
    
    for word, count in notDict.items():
        if word not in magDict:
            flag = False
            break
        if magDict[word] != 0 and magDict[word] < count:
            flag = False
        
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
