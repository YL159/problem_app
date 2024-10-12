'''
Leetcode 1011. Capacity To Ship Packages Within D Days
Given a series of weights and D days to ship them out, find the min capacity of the ship.
Weights should be loaded by their given order in any day.

Similar CodeSignal question:
Given a series of 1*width blocks, put them by given order into k*width1 box layer by layer.
Find min width1 of the box.

This is to partition the weights arr into D non-empty subarr
find the min of max([sum(i day shipping weight)])])

The opt capacity may appear for ith day, not necessarily determined by 1st or last day's
Thus instead of trying out all possible partition, binary search on possible capacity,
and check if this capacity is possible to ship within D days.

Similar to problem 1760, Minimum Limit of Balls in a Bag
Find the limit/min by binary search and use checker as bisect condition
'''
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # checker condition, true if given cap is possible to ship out all weights in given days
        def possible(cap: int) -> bool:
            count = 1
            total = 0
            for n in weights:
                if n > cap:
                    return False
                # greedily add current load to minimize day count
                elif total + n <= cap:
                    total += n
				# wrap today, start another day
                else:
                    count += 1
                    total = n
            return total <= cap and count <= days
        
		# binary search between min/max possible cap
        l, r = max(weights), sum(weights)+1
        while l <= r:
            m = (l+r)//2
            if possible(m):
                r = m-1
            else:
                l = m+1
        return l

