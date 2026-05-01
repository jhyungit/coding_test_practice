# https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

magic = [[8,1,6],
        [3,5,7],
        [4,9,2]]

def lr_mrirror(arr):
    return [row[::-1] for row in arr]

def rotate(arr):
    temp = [[0] * 3 for _ in range(3)]
    for x, ar in enumerate(arr):
        for y, a in enumerate(ar):
            temp[y][abs(x-2)] = a
    return temp

def calc_cost(arr, s):
    cost = 0
    for r in range(3):
        for c in range(3):
            if arr[r][c] != s[r][c]:
                cost += abs(s[r][c] - arr[r][c])
    
    return cost

def formingMagicSquare(s):
    # Write your code here
    answer = float("inf")
    magic_candi = [magic]
    current = magic
    for _ in range(4):
        magic_candi.append(lr_mrirror(current))
        current = rotate(current)
        magic_candi.append(current)
    
    for candidate in magic_candi:
        answer = min(answer, calc_cost(candidate, s))
    
    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
