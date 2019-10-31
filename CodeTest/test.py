#!/bin/python3
# Write a program that adds two numbers prints the sum to STDOUT. 
# Read the input from STDIN. The first line of your input will contain an integer (N) 
# that tells you how many more lines there are in the input. Each of the subsequent N lines contain 2 integers). 
# You need to print the sum of each pair on a separate line of STDOUT.

import math
import os
import random
import re
import sys

#findNumber([3, 1 5,], 5)
# Complete the findNumber function below.
#def findNumber(arr, k):
k = 10
n = int(input())
for _ in range(n):
    a, b = map(int, input().strip().split())
    if a + b == k:
        print('YES')
    else: 
        print('NO')