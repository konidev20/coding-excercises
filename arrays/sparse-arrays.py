#### https: // www.hackerrank.com/challenges/sparse-arrays/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.


def matchingStrings(strings, queries):
    counter = {query: 0 for query in queries}

    for string in strings:
        if string in counter:
            counter[string] += 1

    results = [counter[query] for query in queries]

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
