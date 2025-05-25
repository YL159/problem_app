'''
Leetcode 218. The Skyline Problem
Given a list of rectangle buildings with (left, right, height) metrics, and sorted by left_i
Find the building contour - skyline, as a list of changing points of (start, new_height)

Since each building can start or end anywhere, we can regard each start/end as an event:
	=> for start event, remember where it shall end, and the building height
       for end event, remove any building that ends, and check the tallest building now
    => all events may be a potential contour point
Use heap queue of heights to find the valid max building height at each event position,
try to generate a potential contour point, and validate it in contour array:
	new point's validity is dependent on neighboring last few points, merge/change accordingly

Thus the time complexity is not affected by whether the buildings are sorted or not:
	Individual events should be sorted
    Available heights are in a heap
Time O(nlogn), Space O(n)
'''
import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # for building left event, heap up its height and right info
        # for building right event, process them before any same position left event
        events = buildings + [[r, 0, 0] for _, r, _ in buildings]
        events.sort()
        # min heap for (-height, right)
        heights = []
        res = []
        for left, right, h in events:
            if right != 0:
                # at building start, push its ending info
                heapq.heappush(heights, (-h, right))
            else:
                # at some end event, pop any building ends ON/BEFORE this
                while heights and heights[0][1] <= left:
                    heapq.heappop(heights)
            
            # decide if this event produces an entry to res
            # high: current highest building at position 'left'
            high = -heights[0][0] if heights else 0
            res.append([left, high])
            # merge or change the last entry if possible
            # not proved, but the result tail merge may occur max twice
            while len(res) >= 2:
                cur, cur_h = res[-1]
                pre, pre_h = res[-2]
                if cur != pre and cur_h != pre_h:
                    break
                res.pop()
                if cur == pre:
                    res[-1][1] = max(cur_h, pre_h)
        return res
