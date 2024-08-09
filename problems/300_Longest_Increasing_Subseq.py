'''
Leetcode 300. Longest Increasing Subsequence
Find such subseq in an array of random ints

Idea is to keep track of current longest subseq.
But new # may become new start, or start in the middle of current opt subseq.
New start may have successors more than remains of current subseq. And we want to keep new #

Bisect on sorted array! Bisect left and replace/append, thus it won't change monotonicity of opt subseq.
As if the inserted new element's potential successor will 'etch' out the remains of original opt arr

[1,10,11,2]:
e.g. [1, 10, 11] + 2 --bisect_left got insert idx=1--> [1, 2, 11], still monotonically increasing
Even though 11 appears earlier than 2, that [1, 2, 11] itself is not a valid subseq.
But the length 3 is historically maximal length of such subseq.

Time complexity O(nlogn). Space O(n)
'''
from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # keep track of current increasing subseq
        res = [nums[0]]
        idx = 1
        for n in nums[1:]:
            # for new #, if bisect and idx out of range, means larger than res[-1], append
            # maintaining the monotonicity of res array
            idx = bisect.bisect_left(res, n)
            if idx >= len(res):
                res.append(n)
                continue
            # if bisect and idx inside(even at start) of the subseq, replace it with #
            # replace res element with a non-greater value, maintaining monotonicity
            res[idx] = n
        return len(res)

            