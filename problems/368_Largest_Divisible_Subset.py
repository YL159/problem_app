'''
Leetcode 368. Largest Divisible Subset
Find the largest subset of a list of distinct positive ints, so that:
Each pair of numbers in subset, the larger is multiple of the smaller.

1. DP on the longest div array length of each num. nums.sort()
if nums[i] % nums[i-k] == 0, dp[i] = max(dp[i], dp[i-k]+1) for all 0 <= k < i

2. Record current opt result lists
each new number append to or continue with the longest divisible prefix of current lists
slower, still ~ O(n^2)
'''
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        book = [[nums[0]]]
        for n in nums[1:]:
            candi = []
            middle = False
            for series in book:
                # prepare to append to a candidate list
                if n % series[-1] == 0 and len(series) > len(candi):
                    middle = False
                    candi=series
                    continue
                # prepare to continue with longest prefix
                i = len(series) - 1
                while i >= 0 and n % series[i] != 0:
                    i -= 1
                if i+1 >= len(candi):
                    middle = True
                    candi = series[:i+1]
            candi.append(n)
            if middle:
                book.append(candi)
        
        res = []
        for series in book:
            if len(series) > len(res):
                res = series
        return res
