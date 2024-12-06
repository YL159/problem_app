'''
Leetcode 1775. Equal Sum Arrays With Minimum Number of Operations
Given 2 array of int from [1, 6], find min # of operations to make their sum equal.
1 Operation: change 1 # of 1 of the arrs to any # in [1, 6]

For both lists, greedily increase/decrease max possible change (1->6 or 6->1 is 5, if available):
	depending on available largest changes, either:
         	increase sum of smaller sum arr
			decrease sum of larger sum arr
Thus we maximize the use of each operation with max change possible in either array,
Use heap to always choose the number that brings largest change.
	Min heap for small sum arr. Max heap for big sum arr

Time O(mlog(m) + nlog(n)), space O(m+n)

Sort array and loop with choice also ok
'''
from typing import List
import heapq

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        small, large = (nums1, nums2) if s1 < s2 else (nums2, nums1)
        diff = abs(s1-s2)
        heapq.heapify(small)
        large = [-x for x in large]
        heapq.heapify(large)
        res = 0
        while diff and (small or large):
            # check which heap top # can give max change, greedy
            ch1 = 6 - small[0] if small else 0
            ch2 = -1 - large[0] if large else 0
            ch = max(ch1, ch2)
            if ch >= diff:
                return res + 1
            choice = small if ch1 >= ch2 and small else large
            if choice:
                heapq.heappop(choice)
            diff -= ch
            res += 1
        return -1
