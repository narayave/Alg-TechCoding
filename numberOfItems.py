#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#

# We need 2 loops?
#   Outer loop for start and end indices - n
#   Inner loop for within strings

def numberOfItems(s, startIndices, endIndices):

    res = []
    stack = []

    for starti, endi in zip(startIndices, endIndices):
        cut_string = s[starti-1:endi]

        local_count = 0
        for i in cut_string:
            if i == "|":
                if stack == []:
                    stack.append(0)
                # if first | include in stack
                else:
                    local_count += sum(stack)
                    stack = [0]      # reset
                # if second count stars
            elif i == "*":
                if stack == []:
                    continue
                else:
                    stack.append(1)
            print(i, stack, local_count)

        res.append(local_count)

    return res


# def numberOfItems(s, startIndices, endIndices):

#     item_count = []     # Will hold the list of counts for each item start-end pair

#     for starti, endi in zip(startIndices, endIndices):
#         cut_string = s[starti-1:endi]
#         print(cut_string)
#         star_count = 0
#         star_pipe_count = 0
#         pipe_count = 0
#         for i in cut_string:
#             if i == "*":
#                 star_count += 1
#             elif i == "|":
#                 if (pipe_count > 0) and (pipe_count % 2 == 0):
#                     star_pipe_count += star_count
#                     star_count = 0
#                     pipe_count += 1
#                 else:
#                     pipe_count = 1
#                     star_count = 0

#             print(star_count, star_pipe_count, pipe_count)

#         if (pipe_count > 0) and (pipe_count % 2 == 0):
#             item_count.append(star_pipe_count)
#         else:
#             item_count.append(0)

#     return item_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    print('\n'.join(map(str, result)))
    print('\n')
z
    fptr.close()
