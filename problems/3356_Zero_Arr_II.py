'''
Leetcode 3356. Zero Array Transformation II
Given array nums, and queries of [l, r, val], val >= 0
For each query, # in nums[l, r] can individually subtract maximal val units
Find min first k queries, that after performing them sequencially, nums has only 0s

Method 1. binary search for k in queries. Time O((n+q)*log(q))
Since queries can be partitioned into 2 parts, where after k queries, all later queries guarantees zero arr
Thus binary search for this k. Verifying first k queries takes O(n+q) time using prefix sum on derivatives.

Method 2. at each arr idx, prefix sum on queries as derivatives. Time O(n+q). Inspired by solutions
we don't have to get the accurate earlier prefix sum other than nums[i]
i.e. the derivative array is not accurate EVERYWHERE at ALL TIME
only ACCURATE AT i when VISITING nums[i]
Thus avoid repeatedly starting from first queries and get accurate whole picture.
'''
from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        derive = [0] * (len(nums)+1)
        pref = k = 0
        for i in range(len(nums)):
            while pref + derive[i] < nums[i]:
                if k == len(queries):
                    return -1
                l, r, val = queries[k]
                if r < i:
                    k += 1
                    continue
                # accumulate derivative only at i or l and r+1
                derive[max(l, i)] += val
                derive[r+1] -= val
                k += 1
            pref += derive[i]
        # queries[k] is unprocessed, numerically the same as first k processed
        return k
