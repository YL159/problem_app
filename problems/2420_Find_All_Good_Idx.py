'''
Leetcode 2420. Find All Good Indices
An index is good if:
	left k neighbors are non-increasing
    right k neighbors are non-decreasing
Find all such indices in given nums.

Use sliding window to find valley indices.
We can keep the streak count of non-increasing elements before i, and
	non-decreasing elements before i+k+1
If both counts >= k: those streaks can shrink to make index i "good"

Update right, then check index and update left, to make the loop concise and consistent.
Time O(n), Space O(1)
'''
from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        res = []
        # left: non-increase count just before i
        # right: non-decrease count before i+k
        left, right = 1, 1
        for i in range(1, len(nums)-k):
            # update right count
            if nums[i+k] - nums[i+k-1] >= 0:
                right += 1
            else:
                right = 1
            # check index i
            if left >= k and right >= k:
                res.append(i)
            # update left count
            if nums[i] <= nums[i-1]:
                left += 1
            else:
                left = 1
        return res