'''
Leetcode 1283. Find the Smallest Divisor Given a Threshold
Given an array of numbers, find the smallest divisor, so that the sum(ceil(number/divisor)) <= threshold.

Use double binary search.
Outer loop binary search the divisor in [1, max(nums)] range.
Result of a divisor can be obtained by counting the numbers within (divisor*mult, divisor*(mult+1)] range.
Thus sort the nums beforehand, and bisect on current divisor*mult, count and add the same quotient quickly.
Thus avoid inner O(n) time

Time complexity: max(O(nlogn), O(logx*logn)), x is largest number in nums
Space complexity: O(1)
'''
from typing import List
import math, bisect

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # double binary search
        nums.sort()
        div = nums[-1]
        l, r = 1, nums[-1]
        # binary search on divisors in range [1, max(nums)]
        while l <= r:
            mid = (l + r) // 2
            t = mid
            res = 0
            mult = 1
            prev = 0
            upper_mult = math.ceil(nums[-1]/mid)
            # binary search on divisor*mult in sorted nums
            while mult <= upper_mult:
                cur = bisect.bisect_right(nums, t)
                res += (cur - prev) * mult
                prev = cur
                mult += 1
                t += mid
            if res > threshold:
                l = mid + 1
            else:
                div = min(div, mid)
                r = mid - 1
        return div