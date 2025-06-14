import sys
import math
import heapq
from queue import Queue
import numpy as np
# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( a , b , k , n1 , n2 ) :
    s = set ( )
    for i in range ( n2 ) :
        s.add ( b [ i ] )
    missing = 0
    for i in range ( n1 ) :
        if a [ i ] not in s :
            missing += 1
        if missing == k :
            return a [ i ]
    return - 1


def f_filled ( a , b , k , n1 , n2 ) :
    s = set ( )
    for i in range ( n2 ) :
        s.add ( b [ i ] )
    missing = 0
    for i in range ( n1 ) :
        if not s.intersection ( a [ i ] ) :
            missing += 1
        if missing == k :
            return a [ i ]
    return - 1

if __name__ == '__main__':
    param = [
    ([2, 9, 9, 13, 38, 41, 50, 59, 64, 64, 72, 78, 79, 80, 84, 92, 94, 98, 99],[5, 9, 11, 21, 24, 27, 30, 35, 38, 39, 40, 45, 48, 48, 51, 58, 61, 91, 92],11,9,18,),
    ([-54, -80, -62, 98, -68, 42, 98, 80, -8, -6, 26, 0, -60, -24, -74, -48, 4, -54, 20, 32, 42, 68, -50, 58, -50, 96, -34, 22, 56, -60, -10, -18, 80, 20, -50],[90, -86, -82, 92, -42, -34, 10, -28, -78, 8, 66, 96, -16, -22, -68, -36, -72, 84, -54, -44, -80, -30, 64, 10, -60, -90, 22, 54, -88, 74, -56, 22, -24, -52, 82],24,24,21,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],15,15,11,),
    ([85, 44, 60, 86, 26, 22, 95, 47, 43, 24, 30, 37, 22, 33, 6, 56],[66, 76, 38, 91, 57, 50, 12, 21, 90, 17, 18, 78, 23, 12, 90, 81],12,14,10,),
    ([-32, -18, 2, 54, 72, 92, 94],[-76, -68, -34, -24, 8, 12, 32],6,3,5,),
    ([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],[0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0],29,29,37,),
    ([3, 9, 13, 14, 16, 19, 20, 21, 23, 26, 27, 27, 28, 29, 31, 36, 37, 38, 41, 42, 45, 46, 52, 56, 63, 65, 70, 70, 72, 72, 76, 77, 78, 78, 79, 82, 83, 86, 87, 87, 90, 93, 93, 94, 96, 96, 97, 98],[2, 5, 6, 7, 9, 11, 11, 13, 17, 18, 20, 20, 26, 27, 35, 35, 36, 37, 41, 42, 45, 46, 48, 49, 50, 50, 54, 54, 56, 60, 62, 63, 65, 67, 68, 68, 70, 72, 74, 74, 78, 79, 80, 80, 86, 89, 97, 99],27,39,28,),
    ([-82, -62],[48, 32],1,1,1,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],10,14,12,),
    ([26, 5, 60, 53, 35],[41, 80, 35, 14, 47],3,2,3,)
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
