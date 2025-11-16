'''
Leetcode 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
Given an array of positive ints, with 1 operation:
	choose a pair of neighboring ints, replace one of them with their GCD
Find min # of operations to make the arr all 1. If impossible, return -1

Observation:
1. the neighbor of 1 takes one op to be 1
2. if 1 appear m times in array, it will take n-m operations to make all 1
3. thus if the whole array has GCD > 1, impossible to make all 1, return -1

Method 1, find the shortest subarr that have GCD=1
GCD on neighbors, getting first GCD=1 at t layer downward
	=> subarr of length as small as t+1 can get GCD=1
    => operations = n + t - 1

Method 2, for each arr[i], GCD back to start until GCD=1
collect the shortest length

Time O(n^2), Space O(1)
'''

from typing import List

import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = len(nums)
        ones = 0
        for x in nums:
            ones += x == 1
        if ones:
            return res - ones
        length = len(nums)
        found = False
        for i in range(1, len(nums)):
            j = i-1
            g = nums[i]
            while j >= 0 and g != 1:
                g = math.gcd(g, nums[j])
                j -= 1
            if g == 1:
                length = min(length, i - j)
                found = True
        if not found:
            return -1
        return res + length - 2