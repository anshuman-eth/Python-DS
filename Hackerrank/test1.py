#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a,b):
    for i in range(1):
        for j in range(0,len(b)):
            if a[j]>b[j]:
                x=x+1
            elif a[j]<b[j]:
                
                y=y+1
    print(x,y)
                       
if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)

