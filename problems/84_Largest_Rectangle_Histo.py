'''
Leetcode 84. Largest Rectangle in Histogram
Find the largest rectangle within the histogram formed by non-neg int array

Observation:
The largest rectangle comes from candidate list of:
	rectangle = height[i] * max width stretch from i to left & right
height[i] reach left and right until 1st smaller bar shows up
    => monotonic increasing stack

Method 1, monotonic increasing stack
find how far height[i] can reach to its right.
Record this right-rectangle whenever height[i] is about to pop
Do the same for reversed height arr, add them up and subtract the height itself.

Method 2, improve on method 1, lazy decide each bar's left-right range
poping a height means:
    all heights in [pop, cur] >= popping h
    all heigths in [stack[-1], pop] >= popping h
Thus right end = i, left end = stack top

Time O(n), space O(n)
'''
from typing import List

class Solution:
    # Method 1, monitonic increasing stack, left-right scan
    def largestRectangleArea(self, heights: List[int]) -> int:
        # poping a height => all heights in range [pop, cur] are no less than the poping height
        def monotonic(hs: List[int]) -> List[int]:
            stack = []
            # append 0 to resolve any remaining height idx in stack
            hs.append(0)
            for i, h in enumerate(hs):
                while stack and hs[stack[-1]] > h:
                    pre = stack.pop()
                    hs[pre] = hs[pre] * (i - pre)
                stack.append(i)
            hs.pop()
            return hs
        
        right_ward = monotonic(heights.copy())
        # do the same in reverse, and add
        left_ward = monotonic(list(reversed(heights)))[::-1]
        return max(right_ward[i] + left_ward[i] - heights[i] for i in range(len(heights)))
    
    # Method 2, lazy rectangle decision
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                # lazy decide each stacked prev bars
                height = heights[stack.pop()]
                # accommodate ">="
                left = 0 if not stack else stack[-1]
                # right - left - 1 is rectangle width
                width = i - left - 1
                res = max(res, height * width)
            stack.append(i)
        return res