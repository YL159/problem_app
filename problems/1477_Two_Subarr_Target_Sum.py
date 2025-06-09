'''
Leetcode 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
Given an array of positive ints, find such 2 subarrs with min total length.

First use prefix sum array to find all subarr with sum of target
	=> need to record start-end of these subarr for length
	=> use incremental method, for current index i, check if a target subarr ends here
	=> use dictionary to record seen prefix sum and index for quickly finding start idx of later target subarr

Since all elements >= 1, for some end index, there will be at most 1 start index that sum(arr[start, end]) = target
If generalizing to all integers, for an end index there would be multiple target sum start indices
	=> we can still just pick the largest start index for this end index to examine.
		Ensures smallest current subarr, and largest pool of former target subarrs to choose the smallest as well

For the other former target subarr, we should choose the shortest subarr that ends before current subarr's start
	=> current subarr's start could be anywhere (generally moving right because all elements >= 1), thus need at least O(n) space to store the length info
Since some shortest subarr will be the shortest after its ending index, until some even smaller subarr's length replace it
	=> just use extra array to record the shortest subarr's length SO FAR before each index
Thus to avoid over-lapping.

And finally, record the global smallest sum of combined lengths

Time O(n), Space O(n)
'''
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        # use prefix sum to find target subarr
        # pref_d {prefix sum: appearing index}
        pref_d, pref = {0:-1}, 0
        # optimum array: record length of shortest target subarr that ends before each idx
        # monotonic decreasing
        opt = [n]
        cur_opt = n
        res = n+1 # larger impossible result, i.e. -1
        
        for i, x in enumerate(arr):
            pref += x
            pref_d[pref] = i
            # there is at most 1 match for pref cus arr[i] > 0
            prev = pref - target
            cur_opt = min(cur_opt, i - pref_d.get(prev, i - n))
            opt.append(cur_opt)
            if prev in pref_d and pref_d[prev] >= 0:
                last_end = pref_d[prev]
                # +1 because opt array left padding by an initial n
                res = min(res, opt[last_end+1] + i - last_end)
        
        if res == n+1:
            return -1
        return res
