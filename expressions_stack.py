#!/bin/python

'''
	https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

'''

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(raw_input())

    stack = []
    left = ['[', '{', '(']
    right = [']', '}', ')']
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    for t_itr in xrange(t):
        expression = raw_input()
#        print expression
        for i in expression:
            if i in brackets.keys():
                stack.append(i)
            else:
                if len(stack) != 0 and brackets[stack[-1]] == i:
                    stack = stack[:-1]
                else:
                    stack.append(' ')
                    break

        if len(stack) == 0:
            print 'YES'
        else:
            print 'NO'

        stack = []