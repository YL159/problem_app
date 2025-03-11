'''
Leetcode 1749. Maximum Absolute Sum of Any Subarray
Find the max abs sum of subarrs in an array with +/- numbers

Use Incremental DP method.
A global abs result of current [0...i] subarray. 2 local results of +/- sum including i-th element.

Method 1: record positive/negative parts separately
When iterate each element, maintain local results only if the new element won't break local positivity/negativity,
otherwise restart from local result 0 representing an empty subarray after the new element.
And update global abs result if local results surpass it.

Method 2
Look for greatest discrepancy in pref sum arr, their difference is the optimum abs(sum(subarr))
'''
from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # # global max abs sum
        # res = 0
        # # the +/- sum including the last #.
		# # List is not required to maintain these 2 values.
        # cur_sum = [0, 0]
        # for n in nums:
        #     cur_sum[0] = max(0, cur_sum[0] + n)
        #     cur_sum[1] = min(0, cur_sum[1] + n)
        #     res = max(res, abs(cur_sum[0]), abs(cur_sum[1]))
        # return res

        # method 2, just find the difference between min/max of pref arr
        # min/max initiate as 0 to account for initial pref=0, i.e. subarr from beginning
        s, mi, ma = 0, 0, 0
        for n in nums:
            s += n
            mi = min(mi, s)
            ma = max(ma, s)
        return ma - mi