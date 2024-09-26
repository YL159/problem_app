'''
Leetcode 1590. Make Sum Divisible by P
Remove a subarr (allow [] but not the whole arr) of given arr, and sum(rest) | p

(total sum - subarr[a,b] sum) | p => (sum remainder - (b remainder - a remainder)) | p
=> sum remainder is congruent with (b remainder - a remainder) on p

Record visited prefix sum remainder's latest position, for future shortest subarr length.
If a new remainder can fulfill a record, update the result with subarr length.
'''
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # get prefix sum array's remainder
        rem = [0]
        s = 0
        for n in nums:
            s += n
            rem.append(s % p)
        if s < p:
            return -1
        target = rem[-1]
        if target == 0:
            return 0
        res = len(nums)
        book = {0:0}
        for i in range(1, len(rem)):
            # check if current # can fulfill visited remainder
            # if yes, get its latest position
            fulfill = (rem[i] - target) % p
            if fulfill in book:
                res = min(res, i - book[fulfill])
            # record visited remainder latest position, for later shortest subarr
            book[rem[i]] = i
        if res == len(nums):
            return -1
        return res