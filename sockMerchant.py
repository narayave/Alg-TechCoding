
# HackerRank - https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):

    track = {}
    for i in ar:

        if i in track.keys():
            track[i] += 1
        else:
            track[i] = 1

    res = 0
    for k in track.keys():

        if track[k] < 2:
            continue
        else:
            res += int(track[k] / 2)

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
