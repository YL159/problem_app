'''
Leetcode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Given an integer array and int limit >= 0, find length of above subarr

Observation: max length subarr has max-min within limit
	=> including 1 more will break it
	=> the off edge item is new max/min
Thus we can use sliding window for the state transition:
	use new item as right edge, and use it to decide valid left edge on the run

Method 1. heap to find next min/max of window: O(nlogn)
For window min, holding all window numbers and their idx as tuple inside a max heap.
When getting a new window min:
	if is compatible with current max, safely include it in min heap
    otherwise update window start and pop incompatible max (number or idx < start) from max heap
		untill a max compatible with the new min
Similar for window max update.

Method 2. mon stack to store min/max candidates: O(n)
Similar to method 1 heap solution, but replace heap with monotonic stacks.
Because we are concerned with potential max/min after current max/min's idx
	and other numbers won't affect window's max-min value
    stack will save time on new element traversing the heap to keep in order
'''

from typing import List
import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
		# increasing min stack, decreasing max stack
        minst, maxst = collections.deque(), collections.deque()
        res, start = 0, 0
        for i, n in enumerate(nums):
            # found n is new min of all, need to check if compatible with current max
            if minst and n < nums[minst[0]]:
                while maxst and nums[maxst[0]] - n > limit:
                    # lazy update current window start at imcompatible idx + 1
                    # to get max possible future window size
                    start = maxst.popleft() + 1
            # do the same if n is new max
            elif maxst and n > nums[maxst[0]]:
                while minst and n - nums[minst[0]] > limit:
                    start = minst.popleft() + 1
            # maintain min stack and max stack
            # keep only the latest min/max equal to n thus >= and <=
            # if future new max/min breaks limit, eventually all such equal max/min will pop
            while minst and nums[minst[-1]] >= n:
                minst.pop()
            minst.append(i)
            while maxst and nums[maxst[-1]] <= n:
                maxst.pop()
            maxst.append(i)
            res = max(res, i-start+1)
        return res
