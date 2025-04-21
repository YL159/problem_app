'''
Leetcode 3113. Find the Number of Subarrays Where Boundary Elements Are Maximum
Given an array of positive ints, find the # of subarr where:
Boundary ints are equal AND max of that subarr

Within such subarr, the inner ints are no greater than edge max:
[1,3,4,2,3,1,4,2,4,5]
	 |		 |   |
    3 valid position for 4, choose(2, 3) + 3 = 6 cus each element itself is trivially a valid subarr
And for the 2x 1, the 1st 1 won't be considered anymore cus greater number appear after it
Thus we can use monotonic decreasing stack to keep current min as local max at stack top
and save # of its appearance for rolling sum of valid subarr

Time O(n), Space O(n)
'''
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        # monotonic decreasing stack storing [current min, appearance count]
        stack = []
        res = 0
        for n in nums:
            # n larger than stack top, pop and discard. They won't pair with any future #
            while stack and stack[-1][0] < n:
                stack.pop()
            # n itself count as subarr
            if not stack or stack[-1][0] > n:
                stack.append([n, 1])
            # stack and stack[-1][0] <= n: can't be < n cus the former while loop, thus only ==
            else:
                stack[-1][1] += 1
            # rolling sum of prev appearance to get # of new pairings with current
            res += stack[-1][1]
        return res