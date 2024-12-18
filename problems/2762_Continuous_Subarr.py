'''
Leetcode 2762. Continuous Subarrays
Given an array of int, find # of subarr with max(subarr) - min(subarr) <= 2

We can count distinct subarr by distinct start idx, and sliding window
=> find max length of subarr start at each idx, that its overall fluctuation <= 2
=> # of distinct subarr = end idx j - start idx i

To find the max length of such subarr, we need to keep track of subarr min/max
	=> stop at any new member greater than min by 2 OR smaller than max by 2
	=> can use heap or monotonic stack to keep track of running min/max

Use heap, time O(nlog(n))
Use monotonic stack, time O(n)
Because for heap, we store 'non-essential' # between min/max of a subarr
=> up/down heap takes more time
'''
from typing import List
import collections

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # st1 for increasing stack, storing min
        # st2 for decreasing stack, storing max
        st1, st2 = collections.deque(), collections.deque()
        i, j = 0, 1
        res = 0
        while i < len(nums):
            if j < i:
                j = i+1
            while st1 and st1[0] < i:
                st1.popleft()
            while st2 and st2[0] < i:
                st2.popleft()
            if not st1: # if st1 is empty, st2 must be also empty
                st1.append(i)
                st2.append(i)
            while j < len(nums) and abs(nums[st1[0]] - nums[st2[0]]) <= 2:
                if nums[j] - nums[st1[0]] > 2 or nums[st2[0]] - nums[j] > 2:
                    break
                # maintain increasing stack
                while st1 and nums[st1[-1]] >= nums[j]:
                    st1.pop()
                st1.append(j)
                # maintain decreasing stack
                while st2 and nums[st2[-1]] <= nums[j]:
                    st2.pop()
                st2.append(j)
                j += 1
            res += j - i
            i += 1
        return res
