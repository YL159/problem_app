'''
Leetcode 1248. Count Number of Nice Subarrays
Get the number of subarrays containing exactly k odd numbers

Get the indices of these odd numbers, pairwise find their left and right count of even numbers + 1, multiply
'''

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # get the odd # indices
        odds = []
        for i, n in enumerate(nums):
            if n % 2:
                odds.append(i)
        if len(odds) < k:
            return 0
        res = 0
        for i in range(len(odds)-k+1):
            start, end = odds[i], odds[i+k-1]
            # use index to count the left and right possible choices
            left = start + 1 if i == 0 else start - odds[i-1]
            right = len(nums) - end if i == len(odds)-k else odds[i+k] - end
            res += left * right
        return res