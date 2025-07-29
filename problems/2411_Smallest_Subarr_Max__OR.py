'''
Leetcode 2411. Smallest Subarrays With Maximum Bitwise OR
Given an array of non-negative ints, for each starting index i:
Find length of the smallest subarr starting at i, and has max possible element bitwise OR value.

Observation:
1. arr[i:] will definitely has max OR, then reduce tail # untill subarr OR value changes.
	=> # at right edge must have a unique set bit
2. when move to i+1, the max OR may or may not change.
	=> bit array [111, 100, 11], max OR for arr[0:] = max OR for arr[1:]

Method 1: count set bit frequency + 2-pointer
From observation, window right edge must has a unique bit, while left edge arr[i] doesn't need to have it.
When starting at arr[i+1]:
	if arr[i:] OR value = arr[i+1:] OR value => arr[i] doesn't have unique set bit, right edge remains the same
    if OR value not the same => arr[i] and right edge # both have different unique set bit
		=> right edge shouldn't move left because of unique set bit
        => possibly move right to reach target OR value
Thus the right pointer only goes right, time O(n*log(max))
Steps:
1. from right to left, find target max OR for each arr[i:], O(n*log(max))
2. maintain set bit count for this max OR for each start i, initially count all #
3. remove bit count from right until the total set bits changes
4. remove arr[i] set bit count, increment i
5. check if current set bit same as target, otherwise enlarge window untill target bits are met
Time O(nlog(max)), Space O(n+log(max))


Method 2, backward populating, 1 pass. suggested by hints
Each set bit of a max OR value comes from some earliest # to the right
e.g. suppose subarr from idx i has max OR 1011, find 1st appearance of each set bit to the right of i
thus the min subarr length is max(set bit 1st appearance idx)
	=> traverse from right to left, for each idx i, keep a dictionary of {set bit position: 1st appearance idx to i's right}
    => to reduce space consumption, reuse the dict by getting result after each update
result is max distance of those idx to current i
Time O(nlog(max)), Space O(n+log(max))

nums[i] <= 10^9 < 2^30, thus log(max) < 30
'''

from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # method 2
        # record appearance idx of each set bit
        pos = {b: -1 for b in range(30)}
        # record tail max OR set bits
        # set bits only grow
        bits = set()
        res = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            # update set bit appearance position for nums[i] set bits
            n = nums[i]
            b = 0
            while n:
                if n & 1:
                    pos[b] = i
                    bits.add(b)
                b += 1
                n >>= 1
            # now pos is the dict of 1st appearance of each potential set bit after idx i
            # min subarr length = max(distance from i to set bit's 1st appearance)
            l = 1
            for bit in bits:
                l = max(l, pos[bit]-i+1)
            res[i] = l
        return res