'''
Leetcode 665. Non-decreasing Array
Given an array, check if possible to change at most 1 int to make the array non-decreasing.

Here is a state machine approach.
Check non-decrease of neighboring #, and allow 1 chance to see a decreasing spot.
At decreasing spot, either:
	decrease the peak and make sure its neighbors are also non-decreasing:
		... 2, 5, 4 ... if 2 <= 4, the peak 5 can change to [2,3,4], pass
	increase the pitfall and make sure its neighbors are also non-decreasing:
		... 2, 5, 4, 3 ... here 5 <= 3 is false, the pitfall 4 has no options to change to, fail
Or another decreasing spot but the chance is used. Fail

Time O(n), space O(1)
'''
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # O(n) state machine
        # right padding with -infinity to accommodate nums[-1] reference
        nums.append(float('-inf'))
        chance = True
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i-1]:
                continue
            if chance:
                # reach the real end of nums, the last # can change to arbitrary big #
                if i == len(nums) - 2:
                    return True
                # check if there are options for either spot to change to
                if nums[i] - nums[i-2] >= 0 or nums[i+1] - nums[i-1] >= 0:
                    chance = False
                else:
                    return False
            # run out of chance
            else:
                return False
        return True

