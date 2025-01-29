'''
Leetcode 2317. Maximum XOR After Operations
Given an integer array nums, for each operation:
	choose and update nums[i] with (nums[i] AND (nums[i] XOR x)), pick int x as needed.
Find max XOR of all elements in nums after any number of operations.

nums[i] XOR x <=> we can choose x to make each bit same/different from nums[i]
	thus to get result from 0 (x=nums[i]) to 2^(n+1)-1 (all 1), n digit count of binary nums[i]
nums[i] AND above <=> get a binary number with same/less set bit at the same position as binary nums[i]
	e.g. nums[i] binary 100110 -> possible results are changing some 1s into 0s
XOR all number in nums <=> at each bit: odd/even 0s always get 0; odd 1s get 1, even 1s get 0
Since we want max XOR of all # in nums, we want each bit as 1:
	1 only comes from some number that has this bit as 1
		if even count of number has this bit as 1, we can manipulate x to make it odd count
	0 for all numbers at this bit, then no any x can make any number get this bit as 1

Method 1
Check & collect each number's set bit positions.
Set those positions to 1 for final result.

Method 2
=> As long as there is 1 on some bit, we can preserve it in final result
=> OR all numbers, any bit that has 1 will be preserved.
'''
from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        # choose x so n^x can be any number within n's bit range
        # => n&(n^x) can switch off any set bits in n
        # to get max xor of nums, as long as there is 1 set bit at some position
        # we can preserve odd number of it => result gets as many set bits as possible
        
        # # method 1
        # pos = set()
        # for n in nums:
        #     p = 0
        #     while n:
        #         if n % 2:
        #             pos.add(p)
        #         n >>= 1
        #         p += 1
        # res = 0
        # for p in pos:
        #     res |= 1 << p
        # return res

        # method 2
        # use 'or' to preserve all set bits
        res = 0
        for n in nums:
            res |= n
        return res