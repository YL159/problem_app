from typing import List
'''
134. Gas Station
Running prefix

The real starting point makes sure its 'net cost' array will never be negative.

Thus find the lowest point of accumulated(prefix sum) net cost at each station,
if we 'lift' from the lowest point, the array will all be non-negative.
And thus return its next station as starting point. But if the result station is already non-negative, it will naturally be the start.
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # get the net cost for each segment.
        # space can be optimized to O(1) by merging with later enumeration.
        net = [g-c for g, c in zip(gas, cost)]
        prefix, low = 0, max(net)
        res = 0
        # find the minimum prefix sum of net array
        # we should 'lift' the array to all non-negative from there
        for i, n in enumerate(net):
            prefix += n
            if prefix < 0 and prefix < low:
                low = prefix
                res = i
        # if starting point is the mininum(negative), it will be elevated
        # thus its next stations is the real start
        if net[res] < 0:
            res = (res + 1) % len(gas)
        return res