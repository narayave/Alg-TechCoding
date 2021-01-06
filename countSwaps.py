#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

# Complete the countSwaps function below.


def countSwaps(a):

    cnt = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                cnt += 1
                # swap
                tmp, a[j+1] = a[j+1], a[j]
                a[j] = tmp

    print(f"Array is sorted in {cnt} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
