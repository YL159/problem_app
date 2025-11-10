'''
Leetcode 3542. Minimum Operations to Convert All Elements to Zero
Given a list of non-negative ints, one operation:
	choose a subarr, reduce all min # to 0
Find min # of operations to make the array all 0

Observation: existing 0s can be the min of chosen subarr
	=> avoid including 0 in chosen range
Consider [0,1,2,3,1,4,0,5,1], if we want 1->0 for all 1s, the range will include 0
	=> 0 separates the range => smallest ints separates any larger range if interspersed.
Thus for [1,2,3], [1,4], [5,1], each can safely 1->0: [0,2,3], [0,4], [5,0]
And separates them by 0 again

When climbing from smaller ints to larger ints, we are performing monotonic stack operation!
	=> any int greater than current can be included into current subarr selection
    => new smaller ints can make the stack pop larger ints, each unique larger int takes 1 op
    => keep idempotency of consecutive same ints <=> stack ints should be unique
And don't forget the remaining unique ints in stack, or right padding nums with 0
'''

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for n in nums:
            # when cur is smaller than stack top
            # each unique stack top int requires 1 op
            while stack and stack[-1] > n:
                stack.pop()
                res += 1
            # stack is idempotent for consecutive same n or any 0
            if n != 0 and (not stack or stack[-1] != n):
                stack.append(n)
        # wrap up remaining unique ints in stack
        return res + len(stack)