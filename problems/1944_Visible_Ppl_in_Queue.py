'''
Leetcode 1944. Number of Visible People in a Queue
Given a list of distinct people heights in a queue, find how many ppl can 1 person see to the right of him.
'can see' means all persons between person i:j are shorter than min of person i & j.

Intuitively we can check right monotonic decreasing stack of a person(p).
If he is taller than stack top p, he can definitely see that p.
Pop until some1 taller than him or empty stack. Count the popped and +1 if stack not empty (the 1st taller)

Any skipped shorter ps won't be seen because there are taller ps between cur p and that short p.
i.e. only count those popped out of the stack, not any p in between.

The result is related to the working state of the stack, and checking visibility to the right,
thus following the construction of monotonic decreasing stack, work on results backward as well.
Time O(n), space O(n)
'''
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # monotonic decreasing stack from right of arr, check ppl in reverse
        res = [0]
        stack = [len(heights)-1]
        i = len(heights) -2
        while i >= 0:
            count = 0
            # pop those are shorter than heights[i], they are visible
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                count += 1
            # count the 1st taller p
			# cus all ps in between are shorter than heights[i],thus this p visible
            if stack:
                count += 1
            stack.append(i)
            res.append(count)
            i -= 1
        res.reverse()
        return res