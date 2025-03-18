'''
Leetcode 2401. Longest Nice Subarray
Find the length of longest subarr:
	Bit-AND between every num pair in subarr is 0

Method 1: Bit-OR preserve seen set bits
new b AND some prev n gets non-0 => some set bit of b shows up in this prev n
we can preserve all set bits of a subarr (OR of subarr) to check if it AND-collides with new b
thus keep prefix OR of nums, keep track of latest number idx that has some set bit
Time O(nlog(max(nums)))

Method 2: Sliding window XOR and sum
a&b = 0 => a^b = a+b. maintain window xor and window sum. xor = sum => valid subarr
Time O(n)

Method 3: Sliding window OR and XOR
a&b = 0 => a^b = a|b. maintain window OR, when OR & n, xor from window left till OR & n = 0
Time O(n)
'''
from typing import List
import collections

class Solution:
    # def longestNiceSubarray(self, nums: List[int]) -> int:
    #     bits = collections.defaultdict(int)
    #     # prefix OR of nums
    #     por = 0
    #     res = 1
    #     last_collide = -1
    #     for i, n in enumerate(nums):
    #         AND = por & n
    #         # idx: biggest index of nums that collides with n
    #         idx = -1
    #         pos = 0
    #         while AND:
    #             if AND & 1:
    #                 idx = max(idx, bits[pos])
    #             AND >>= 1
    #             pos += 1
    #         # result can't extend beyong last_collide.
    #         # nums[3] newly collide with nums[8], thus AND-valid subarr ending at nums[12] can't extend beyond idx=3
    #         last_collide = max(last_collide, idx)
    #         res = max(res, i - max(last_collide, idx))
    #         # update idx record of every set bit of current n
    #         cur = n
    #         pos = 0
    #         while cur:
    #             if cur & 1:
    #                 bits[pos] = i
    #             cur >>= 1
    #             pos += 1
    #         por |= n
    #     return res
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        XOR, s = 0, 0
        l, r = 0, 0
        res = 1
        while r < len(nums):
            # extend window size till end or XOR=s breaks
            while r < len(nums) and XOR == s:
                XOR ^= nums[r]
                s += nums[r]
                r += 1
            # r-l, -1 only when prev while exits because of XOR != s, where r is 1 ahead of nums[invalid]
            res = max(res, r-(XOR != s)-l)
			# maintain window XOR and sum
            while l < r and XOR != s:
                XOR ^= nums[l]
                s -= nums[l]
                l += 1
        return res