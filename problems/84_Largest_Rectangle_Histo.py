'''
Leetcode 84. Largest Rectangle in Histogram
Find the largest rectangle within the histogram formed by non-neg int array

Theorem: The largest rectangle comes from candidate list of:
	rectangle = height[i] * max width stretch from i to left & right

Use monotonic increasing stack to find how far height[i] can reach to its right.
Record this right-rectangle whenever height[i] is about to pop
Do the same for reversed height arr, add them up and subtract the height itself.
Time O(n), space O(n)
'''
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monitonic increasing stack
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