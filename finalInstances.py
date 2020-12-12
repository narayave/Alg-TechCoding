#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'finalInstances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER instances
#  2. INTEGER_ARRAY averageUtil
#
import math
# Solution can definitely be O(n), no reason to go through the list multiple times


def finalInstances(instances, averageUtil):
    # Write your code here
    print(instances, len(averageUtil), averageUtil)

    # Loop runs till we reach this value
    max_length_of_utils = len(averageUtil)
    i = 0       # Single pointer needed to run through the list

    while i < max_length_of_utils:

        print (averageUtil[i])
        if averageUtil[i] < 25:
            # First update the number of instances
            if instances == 1:
                i += 1
            else:
                instances = math.ceil(instances / 2)
                # Update pointer to include 10 secs
                i += 10     # 10 plus we want to move one more step
        elif (25 <= averageUtil[i]) and (averageUtil[i] <= 65):
            # Don't need to do anything special here
            i += 1
        elif averageUtil[i] > 65:
            # First multiple by 2
            instance_limit = 2 * (10**8)
            if (instances * 2) < instance_limit:
                instances = instances * 2
                # Update pointer to include 10 secs
                i += 10     # 10 plus we want to move one more step
            else:
                i += 1

    return instances


if __name__ == '__main__':


1. I knew from the beginning that we only need to traverse the list once using a single pointer. Each loop will check the value at the pointer's location. The conditions are just if statements to check the utilization.

I read the problem a couple times and went over the given examples. I also have a whiteboard that I used to run through my own example.


2. The runtime complexity is O(n) because the list is traversed only once.
