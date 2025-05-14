'''
Leetcode 57. Insert Interval
Given a sorted-by-start list of non-overlapping intervals, and a new interval
Insert new interval into the list and merge overlapping intervals

Use the fact that intervals are sorted by start
iterate invervals (or bisect by end) to find the interval that must overlap/come after the new interval
Resolve former intervals trivially, and merge all overlapping intervals by updating new end.
untill end < next interval's start or loop finishes

Time O(n) since we returning the new interval list anyways
Space O(n) if considering returning new array
'''
from typing import List
import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        l, r = newInterval
        idx = bisect.bisect_left(intervals, l, key=lambda x: x[1])
        res.extend(intervals[:idx])
        if idx == len(intervals):
            res.append(newInterval)
            return res
        
        # now newInterval must hook with intervals[idx]
        start, end = min(intervals[idx][0], l), r
        while idx < len(intervals) and intervals[idx][0] <= end:
            end = max(intervals[idx][1], end)
            idx += 1
        res.append([start, end])
        res.extend(intervals[idx:])
        return res
