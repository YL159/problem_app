'''
Leetcode 3355. Zero Array Transformation I
Given a non-negative number array, check if it can become zero array by processing all queries:
	From queries[i] = [l, r] range, select some idx and reduce nums[idx] by 1
Return True if nums can become zero array.

Sequentially or not, after all queries:
	each nums[i] can maximally reduced if select every idx within a query range
	=> just check if nums[i] is no greater than this maximal possible reduction
Thus use line sweep for all queries, and make prefix sum to get tha maximal reduction at idx

Time O(q+n), Space O(n)
'''
from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        reduction = [0] * (len(nums)+1)
        for l, r in queries:
            reduction[l] += 1
            reduction[r+1] -= 1
        for i in range(len(nums)):
            if nums[i] > reduction[i]:
                return False
            reduction[i+1] += reduction[i]
        return True
