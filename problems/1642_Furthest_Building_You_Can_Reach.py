'''
Leetcode 1642. Furthest Building You Can Reach
Given a list of building heights, and some ladders and bricks. Start from building[0]:
	move to next building <= current: no cost
	next building > current: use 1 ladder or height diff bricks
Find furthest reachable building when using resources optimally

Implicit backtrack by swapping used ladders with bricks, and use that ladder at current pos
	=> bricks should be enough for 1 used ladder (greedy min diff of used => heap),
		or if current diff smaller than min used ladder, enough for current diff
Thus use ladders first, then swap min ladder with bricks
Time O(nlog(n)), space O(n)
'''
from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # suppose use all ladders at first
        # then swap 1 ladder that cover min diff to using bricks
        hp = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            # use ladder first
            if ladders > 0:
                ladders -= 1
                heapq.heappush(hp, diff)
                continue
            # use brick for swapping prev min ladder is optimum
            elif hp and hp[0] <= diff:
                if bricks >= hp[0]:
                    bricks -= hp[0]
                    heapq.heapreplace(hp, diff)
                else:
                    return i
            # use brick for current diff is optimum
            elif bricks >= diff:
                bricks -= diff
            else:
                return i
        return len(heights) - 1
