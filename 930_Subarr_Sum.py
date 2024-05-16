'''
930. Binary Subarrays With Sum
Find count of all subarrays sum to goal
subset of problem 560 https://leetcode.com/problems/subarray-sum-equals-k/
pfs is workable here as well

With enhanced moving frame (sliding window), check each tight 1...1 subarray's neighboring options and add to result.
Since each of these subarray has different 1...1 core, uniqueness guaranteed.

Treat goal = 0 differently, because 0 plus itself is still 0, the goal.
Unlike 1 plus itself will deviate from goal.
'''

from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 0:
            return self.subZero(nums)
        
        # get the indices of each 1 in nums
        # counting 0s is now replaced by index diff
        ones = [i for i in range(len(nums)) if nums[i]]
        if len(ones) < goal:
            return 0

        res = 0
        start, end = 0, goal-1
        # each tight 1...1 subarr got left and right independent choices of 0s +1
        while end < len(ones):
            left = ones[start] - ones[start-1] if start > 0 else ones[start]+1
            right = ones[end+1] - ones[end] if end < len(ones)-1 else len(nums)-ones[end]
            res += left*right
            start += 1
            end += 1
        return res

    # special treatment for goal = 0
    def subZero(self, nums: List[int]) -> int:
        res = 0
        count = 0
        # calculate each 0 pockets
        for n in nums:
            if n:
                res += (count + 1) * count // 2
                count = 0
            else:
                count += 1
        else:
            res += (count + 1) * count // 2
        return res