import sys
import math
import heapq
from queue import Queue# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( arr , n ) :
    um = { }
    sum = 0
    maxLen = 0
    for i in range ( n ) :
        if arr [ i ] == 0 :
            sum += - 1
        else :
            sum += 1
        if ( sum == 1 ) :
            maxLen = i + 1
        elif ( sum not in um ) :
            um [ sum ] = i
        if ( ( sum - 1 ) in um ) :
            if ( maxLen < ( i - um [ sum - 1 ] ) ) :
                maxLen = i - um [ sum - 1 ]
    return maxLen


def f_filled(arr, n):
        um = {}
        sum = 0
        maxLen = 0
        for i in range(n):
            sum += arr[i] == 0? -1 : 1
            if sum == 1:
                maxLen = i + 1
            else:
                if sum not in um:
                    um[sum] = i
                else:
                    if maxLen < i - um[sum]:
                        maxLen = i - um[sum]
        return maxLen

if __name__ == '__main__':
    param = [
    ([6, 10, 31, 35],2,),
    ([4, 88, -72, 28, -54, 32, -34],6,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1],4,),
    ([39, 22, 15, 10, 34, 87, 46, 83, 74, 77, 61, 90, 43, 67, 64, 72, 92, 52, 68, 53, 67, 32, 82, 76, 76, 47, 74, 47, 8, 80, 85, 58, 75],26,),
    ([-82, -58, -50, -30, -14, -4, -2, -2, 0, 22, 36, 58, 70, 80, 80, 82, 84, 90],14,),
    ([1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1],7,),
    ([4, 11, 17, 21, 21, 22, 30, 31, 36, 37, 39, 40, 45, 46, 47, 48, 52, 53, 53, 60, 60, 65, 66, 66, 67, 67, 87, 88, 91, 97],29,),
    ([-4, -60, -78, -50, 64, 18, 0, 76, 12, 86, -22],7,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],17,),
    ([4, 39, 50, 37, 71, 66, 55, 34, 1, 41, 34, 99, 69, 31],11,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        import copy
        p2 = copy.deepcopy(parameters_set)
        filledres = f_filled(*parameters_set)
        goldres = f_gold(*p2)
        if filledres == goldres:
            n_success+=1
        else:
            if set([filledres,goldres]) <= set([float("inf"),sys.maxsize,2147483647]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize,-2147483648]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
