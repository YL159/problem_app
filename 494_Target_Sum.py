'''
Leetcode 494. Target Sum
Assign + or - to each number in nums, count number of ways to sum as target

DP or Incremental, using hashtable to keep track of source count of each possible sum
'''

from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if target > total or target < -total:
            return 0
        total = 0
        book1, book2 = {}, {}
        # initialize book1 for 1st number, combine 0 & -0 starts
        if nums[0] == 0:
            book1[0] = 2
        else:
            book1[nums[0]] = 1
            book1[-nums[0]] = 1
        for n in nums[1:]:
            # for each new # get all possible sums and source counts to book2
            for k in book1:
                if k + n in book2:
                    book2[k+n] += book1[k]
                else:
                    book2[k+n] = book1[k]
                if k - n in book2:
                    book2[k-n] += book1[k]
                else:
                    book2[k-n] = book1[k]
            book1, book2 = book2, {}
        return book1.get(target, 0)
    