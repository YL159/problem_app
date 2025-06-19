'''
Leetcode 862. Shortest Subarray with Sum at Least K
Given an array of ints(+/-), find the shortest subarr that sums >= k

Sliding window is only working for all positive ints.
It guarantees monotomic increasing prefix sum array, shrinking window <=> smaller sum

Considering negative numbers, alter sliding window with monotonic deque,
thus keeping the property of shrinking 'window' <=> smaller sum

Method:
Use prefix sum for quick subarr sum check.
Use monotonic increasing deque on prefix sum array, que is sorted thus 'sliding window' works
	if pref[j] - pref[earlier i] >= k, then a pref[j] - pref[later i'] also >= k
	definitely give better (smaller) subarr.
'''
from typing import List
import collections

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pref = [0]
        for n in nums:
            pref.append(pref[-1] + n)
        que = collections.deque()
        res = len(nums)+1
        
        for i, p in enumerate(pref):
            # check & pop any smaller indices in que that satisfy >= k sum
            while que and p - pref[que[0]] >= k:
                res = min(res, i - que.popleft())
                
            # maintain monotonic increasing deque by keeping the bottom increasing pref indices
            while que and pref[que[-1]] >= p:
                que.pop()
            que.append(i)

        if res == len(nums)+1:
            return -1
        return res