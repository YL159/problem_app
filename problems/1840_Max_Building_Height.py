'''
Leetcode 1840. Maximum Building Height
Given a list of building height restrictions[[i, lim]...] with:
    Neighboring buildings have height difference at most 1.
    Position 1 has height 0.
Find the max building height if building from 1 to n positions.

Observations:
1. Each new restriction may affect prev decisions, better sort restrictions and visit by order.
2. Visit each limit and check if compatible with prev recorded "reachable" limit

e.g. suppose recorded (3, 4), idx 3 can reach building height 4
yet new limit (4, 1) makes prev (3, 4) not reachable, thus pop (3, 4)
and check with earlier records.
    => if prev record is compatible with (4, 1), it means some high building exists in between.
    => when the buildings cascade to idx 3, the height must be <= 4
    Otherwise (3, 4) would be valid in the first place.
    => popping (3, 4) is safe.

Thus we first sort the restrictions
Visit each limit and try to record each position's current reachable limit
    => check with stack top record, see if they can meet in between.
    => meet in between: highest building taller than both ends, current limit reachable
    => meet to the right of current limit: current limit >= staircase height at current idx.
    => meet to the left of prev limit: prev should pop because recorded height is not feasible
Once the reachable limit stack is found, iterate and find the max building defined by these true limits.

Time O(nlogn), Space O(n)
'''

from typing import List

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # iterate restrictions by order of idx
        restrictions.sort()
        # stack of true and reachable limitations. (1,0) will never pop
        stack = [(1, 0)]
        for i, cur in restrictions:
            p, prev = stack[-1]
            # find the highest building's idx offset to idx p
            # between current lim and prev recorded lim, could be xx.5
            hi = (cur + (i-p) - prev) / 2
            while hi < 0:
                stack.pop()
                p, prev = stack[-1]
                hi = (cur + (i-p) - prev) / 2
            # offset is between cur i and prev p, current lim is reachable
            if hi <= i-p:
                cur_h = cur
            # offset to the right of i, current lim calculated from prev
            else:
                cur_h = prev + i-p
            stack.append((i, cur_h))
        
        # iterate the true lim stack to find global max height
        p, prev = 1, 0
        max_h = 0
        for i, cur in stack[1:]:
            hi = (cur + i-p - prev) // 2
            max_h = max(max_h, prev + hi)
            p, prev = i, cur

        # clean up tail increment till n
        if stack[-1][0] < n:
            p, prev = stack[-1]
            max_h = max(max_h, prev + n-p)
        return max_h