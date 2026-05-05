'''
Leetcode 55. Jump Game
Given a list of int nums, from nums[i] you can jump to any idx within nums[i] steps
start from nums[0], check if you can reach nums[-1]

Observation:
Zigzag or jump to left can be ignored, because back tracking makes no progress

Standing on index i comes from several possible left indices
<=>
Each index i can cover some right indices, and they have their limits to

Method 1, from nums[-1], check furthest left possible source
If multiple i can reach some j > i, then greedily choose the largest i that reach j
    => find as many source idx as possible, in order to try to cover idx=0
Search from list end to start.

Method 2, from nums[0], check each cover range's next cover range
Since next cover range may overlap with current range
    => avoid by searching from prev range's right limit

Time O(n), Space O(1)
'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Method 1. start from end index, greedily find left-nearest reachable source
        end = len(nums)-1
        prev = end - 1
        while prev >= 0:
            if nums[prev] >= end - prev:
                end = prev
            prev -= 1
        return end == 0


    def canJump(self, nums: List[int]) -> bool:
        # Method 2. start from index 0, linearly find next cover range
        cur, lim = 0, nums[0]
        while cur != lim and lim < len(nums)-1:
            new_lim = lim
            # inner loop check only fresh nums[i], thus avoid revisiting checked idx
            for i in range(cur+1, min(lim+1, len(nums))):
                new_lim = max(new_lim, i + nums[i])
            cur, lim = lim, new_lim
        return lim >= len(nums) - 1