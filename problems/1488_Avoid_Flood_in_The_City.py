'''
Leetcode 1488. Avoid Flood in The City
There are many lakes initially empty. Given int array rains:
    rains[i] = 0 means no rain on ith day
    rains[i] > 0 means raining on rains[i] lake on ith day
A lake would be full if rained on it, and takes 1 sunny day to drain it.
1 sunny day can only drain 1 lake. Drain an empty lake makes no difference
Arrange a result array of draining strategy so that no lake would flood.
result[i] = -1 if ith day is raining. result = [] means no such strategy

Try greedy asignment:
Greedily asign the last available sunny day after its prev rains to drain that lake.
    Wrong if the last sunny day is the only chance for some other full lake:
    [1,0,2,0,1,2], the 2nd sunny day should drain lake 2 not 1

Greedily asign the earliest available sunny day when rain again on a full lake:
    Wrong if the earliest available sunny day is before the day that lake was rained.

=> maybe find the earliest available sunny day AFTER the day that lake was rained
    thus the later sunny days are reserved as many as possible for lately full lakes

Sequentially collect all sunny days, for binary search for the sunny day AFTER the full lake x
=> that sunny day may have been asigned, need to find the next available sunny day
=> linear search? Then the algorithm degenerate into O(n^2) time, binary search makes little impact

=> disjoint set, union find the next available sunny day
Each sunny day initially available, a node points to itself as root of its set
Once a sunny day is asigned, it should union with its next available sunny day, points to the other set

Time about O(nlogn), Space O(n)
'''

from typing import List

import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        # disjoint sunny days, (rains[] day idx, idx of nex available sun), initially idx points to itself
        sunny = []
        full = {}
        res = [-1] * len(rains)

        # find the next available sunny day's index in sunny array
        def find_next(index: int) -> int:
            if index == len(sunny):
                return len(sunny)
            # given index inside sunny index range
            if sunny[index][1] == index:
                return index
            sidx, nidx = sunny[index]
            # recursively union and find next available sunny day
            sunny[index] = (sidx, find_next(nidx))
            return sunny[index][1]


        for i, x in enumerate(rains):
            if x == 0:
                # build sunny day array on the way, iterate rains only once
                sunny.append((i, len(sunny)))
                continue
            
            if x in full:
                # find the earliest sunny day AFTER lake x last full
                sidx = bisect.bisect(sunny, (full[x], -1))
                # find the earliest AVAILABLE sunny day
                nidx = find_next(sidx)
                if nidx == len(sunny):
                    return []
                ridx, nx = sunny[nidx]
                res[ridx] = x
                # lazy point this sunny day to its next sunny day
                sunny[nidx] = (ridx, nx + 1)
            
            # lake x drained and allow to get rained
            # update lake x full day
            full[x] = i
        
        # lazy update unused draining opportunities to drain lake 1
        for i, x in enumerate(rains):
            if x == 0 and res[i] < 0:
                res[i] = 1
        return res