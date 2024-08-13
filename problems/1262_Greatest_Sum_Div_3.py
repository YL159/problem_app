'''
Leetcode 1262. Greatest Sum Divisible by Three
Given an array, find the greatest sum of its elements that is divisible by 3.

Use O(1) space DP on all possible remainders (0, 1, 2) of current sums
'one' is the current sum of elements, 'one' % 3 = 1, etc.

New sum named 'one' comes from:
Previous 'one' sum, previous 'zero' sum + x(%3=1), previous 'two' sum + y(%3=2)
'''
from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # current sum of a subsequence that remains 0, 1, 2
        zero, one, two = 0, float('-inf'), float('-inf')
        for n in nums:
            r = n % 3
            # update new sums by converging different sources
            if r == 0:
                zero, one, two = zero + n, one + n, two + n
                continue
            z1, o1, t1 = zero, one, two
            if r == 1:
                # new sum|0 comes from:
                # prev sum|0, and prev sum|2 plus n|1
                z1 = max(zero, two + n)
                o1 = max(one, zero + n)
                t1 = max(two, one + n)
            else:
                z1 = max(zero, one + n)
                o1 = max(one, two + n)
                t1 = max(two, zero + n)
            zero, one, two = z1, o1, t1
        return zero

'''
Another greedy solution:
The greatest sum must be close to sum(nums)
Just remove smallest numbers that contribute to the remainder of sum % 3
'''
# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         s = 0
#         ones = [float('inf'), float('inf')]
#         twos = [float('inf'), float('inf')]
#         for n in nums:
#             s += n
#             r = n % 3
#             if r == 1:
#                 if n < ones[0]:
#                     ones = [n, ones[0]]
#                 elif n < ones[1]:
#                     ones[1] = n
#             elif r == 2:
#                 if n < twos[0]:
#                     twos = [n, twos[0]]
#                 elif n < twos[1]:
#                     twos[1] = n
#         rem = s % 3
#         if rem == 1:
#             s -= min(sum(twos), ones[0])
#         elif rem == 2:
#             s -= min(sum(ones), twos[0])
#         return s