'''
Leetcode 2444. Count Subarrays With Fixed Bounds
Given minK and maxK, find # of subarrs of given nums that:
min(subarr) = minK, and max(subarr) = maxK

Observe that such subarr won't include any # > maxK or < minK
	=> those off-bound # are barriers for potential subarr
	=> find target subarr within each of these "pockets"
    
Each target subarr contains at least 1 minK and maxK
	=> collect idx of minK/maxK within each pockets
    
For each start, find the idx of earliest minK and maxK within that pocket
their max is the min end, valid till the end of pocket
because each of such subarr has unique end. And between different starts, have unique start

Time O(n), Space O(n)
'''
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        
        # count valid subarr for each start
        def findSub(i: int, j: int) -> int:
            if i >= j or not mi or not ma:
                return 0
            start, mi_idx, ma_idx = i, 0, 0
            result = 0
            # use mi/ma idx to make sure at least 1 minK/maxK included from start
            while start < j and mi_idx < len(mi) and ma_idx < len(ma):
                cur_end = max(mi[mi_idx], ma[ma_idx])
                result += j - cur_end
                if start == mi[mi_idx]:
                    mi_idx += 1
                if start == ma[ma_idx]:
                    ma_idx += 1
                start += 1
            return result
        
		# divide nums into subarrs within minK/maxK, nums[start:end]
        start, end, res = 0, 0, 0
        # mi/ma record mink/maxk idx within each pocket
        mi, ma = [], []
        while end < len(nums):
        	#  any smaller/larger are barriers
            if nums[end] > maxK or nums[end] < minK:
                res += findSub(start, end)
                start = end + 1
                mi, ma = [], []
                end += 1
                continue
            if nums[end] == maxK:
                ma.append(end)
            if nums[end] == minK:
                mi.append(end)
            end += 1
        res += findSub(start, end)
        return res