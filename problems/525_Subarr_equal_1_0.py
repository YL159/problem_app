'''
Leetcode 525. Contiguous Array
Given an array of 0-1s, find the longest subarray with equal # of 0-1s

Idea is each 0 cancels 1 of previous 1 counts.
When this count shows a # seen before, we know the subarr in between must have equal # of 0-1s
'''
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # each 0 cancels count of 1, also goes negative
        res = 0
        # 1-0 count: first position
        book = {0: -1}
        count = 0
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            else:
                count -= 1
            if count in book:
                res = max(res, i - book[count])
            else:
                book[count] = i
        return res