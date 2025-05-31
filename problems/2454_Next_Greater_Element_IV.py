'''
Leetcode 2454. Next Greater Element IV
Given a list of ints nums, find each element's second subsequent larger element.
[2,4,6,5], 2 got 6 as second larger, 4 got 5 as second larger, -1 for 6 & 5

Use monotonic decreasing stack and record [nums[i], i, received larger?]
For a new larger element, pop any smaller elements in stack:
	if any of them haven't received a larger element, change it to 'received' and restack in order
    those that had received one, nums[i] is their result
Thus each nums[i] can enter stack at most twice
Time O(n)
'''
from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i, n in enumerate(nums):
            tmp = []
            while stack and stack[-1][0] < n:
                x, idx, received = stack.pop()
                if received:
                    res[idx] = n
                else:
                    tmp.append([x, idx, True])
            stack.append([n, i, False])
            # restack updated elements in original order
            stack.extend(tmp[::-1])
        return res
