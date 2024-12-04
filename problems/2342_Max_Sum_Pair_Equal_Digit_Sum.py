'''
Leetcode 2342. Max Sum of a Pair With Equal Sum of Digits
Given a list of positive ints, find max sum of 2 int of different idx,
	that their digit sums are the same

Precompute digit sum of each #, greedily keep the largest # of some digit sum as dictionary
If a future # gets a digits sum seen before, update global result for their sum

Time O(n), but actually O(n*len(digit)), space O(n)
'''
from typing import List
import collections

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # precompute digit sum for each #, store {visited sum: greatest # visited}
        book = collections.defaultdict(int)
        res = -1
        for n in nums:
            s = self.digitSum(n)
            if s in book:
                res = max(res, book[s] + n)
            book[s] = max(book[s], n)
        return res
    
    def digitSum(self, n: int) -> int:
        res = 0
        while n:
            res += n % 10
            n //= 10
        return res