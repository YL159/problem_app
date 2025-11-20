'''
Leetcode 89. Gray Code
Given digit count n, rearrange [0, 2^n-1] ints so that:
	array starts with 0, array[0] and array[-1] connect as a circle array
	neighboring int's binary differ exactly 1 bit
Give such an array

e.g. n=3
000, 001, 010, 011, 100, 101, 110, 111
whenever adding 1 carries to next digit, neighbors differ more than 2 digits
000, 001, 010, 011,| 111, 110, 101, 100
This solves the half point joint 011 -> 111, why not solve each part's local half points?
000, 001,| 011, 010,| 110, 111, 101, 100
for last 2 digits, their change is symmetric, or progressively flipping the same positions
	=> recursively flipping smaller tails
	=> flip is xor 2^x

So we recursively flipping tail x digits
flip the x+1 position
and again flip tail x digits
'''

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # power[i] is 2^(i-1)
        power = [1, 1]
        for _ in range(n):
            power.append(power[-1] << 1)
        res = [0]

        def flip(tail: int) -> None:
            if tail == 0:
                return None
            flip(tail - 1)
            res.append(res[-1] ^ power[tail])
            flip(tail - 1)
        
        flip(n)
        return res