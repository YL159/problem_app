'''
Leetcode 1354. Construct Target Array With Multiple Sums
Start from a list arr of 1, for each operation:
	replace arr[i] with sum(arr), i is free to choose
Find if possible to construct arr to target array with any # of operations.

Observation:
target number (not 1) showing twice is impossible
arr sum is always increasing

If building from [1,...], each replace choice will affect future increment possibilities

As hint suggests, work from largest target in a deterministic way:
[1,5,9], 9 must be sum of [1,5,x] => x = 9-(1+5) = 3
[1,5,3], 5 = sum(1,3,x) => x = 1
[1,1,3], 3 = sum(1,1,x) => x = 1 valid
Thus use max heap of target numbers and update untill all 1

Optimization:
the calculated x may still be the largest in current target array
	=> use mod remaining sum to fast forward the process
Time O(nlog(n)), Space O(n)
'''

from typing import List

import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        hp = [-x for x in target]
        heapq.heapify(hp)
        s = sum(target)
        while hp and hp[0] < -1:
            t = -heapq.heappop(hp)
            other = s - t
            if other == 1:
                return True
            if other == 0:
                return False
            # t0 is the original x replaced by t the sum, subtract at least once
            # if t is too large, that t0 is still the largest
            # subtract untill smaller than other (<= new max -hp[0])
            t0 = t % other
            if t0 == 0 or t0 == t:
                return False
            s -= t - t0
            heapq.heappush(hp, -t0)
        
        return True
