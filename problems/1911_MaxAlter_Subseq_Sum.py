'''
Leetcode 1911. Maximum Alternating Subsequence Sum
Find a subsequence of given array, that its sum(even-index) - sum(odd-index) is maximal.

Choose local peaks for even indexed #, and subsequent valleys for odds.
Since all # are positive, subseq length must be odd. i.e. ends with a peak.
'''
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # make sure there is a peak near the end of nums
        nums.append(nums[-1]-1)
        diff = []
        # create a difference array of nums, to check the monotonicity of array
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i-1])
        increase = True
        even, odd = 0, 0
        for i, d in enumerate(diff):
            # d < 0 and previously increasing means nums[i] is local peak
            if d < 0 and increase:
                increase = False
                even += nums[i]
            # d > 0 and previously decreasing means nums[i] is local valley
            elif d > 0 and not increase:
                increase = True
                odd += nums[i]
            # ignore d = 0, because consecutive same numbers in nums won't affect local optima
        return even - odd