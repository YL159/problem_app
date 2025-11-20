'''
Leetcode 757. Set Intersection Size At Least Two
Given a list of intervals, each interval represents all ints between [start, end]
Find the smallest length of an intersection set, that each above interval has at least 2 ints in the set.
Each interval contains at least 2 ints

Usually we sort the intervals by end, then by start, to group related intervals together and in sequence.
For each interval, we should either choose 2 ints, or greedily reuse chosen ints (prev 2 choices):
	if choose 2 ints, it must be that prev 2 choices are not in range
		=> greedily choose the largest 2 ints (end-1, end)
    if can reuse 1 of prev choices
    	=> larger choice must be the one to reuse, smaller choice is out of range, since the intervals are sorted
		=> smaller choice is now prev larger, update larger choice with current end
        if current end = prev larger, smaller choice should step back by 1
	if can reuse both prev choices
		greedily do nothing
Time O(nlog(n)), Space O(1)
'''

from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sort by end, then start
        intervals.sort(key=lambda t: (t[1], t[0]))
        count = 0
        c1, c2 = -1, -1
        # reuse existing choices for new intervals
        # greedily choose right edge numbers for each interval if can choose
        for start, end in intervals:
            # prev choice outdated, choose 2x far right of current interval
            if c2 < start:
                count += 2
                c1, c2 = end-1, end
            # c2 must be inside, update c1 to c2, or c2-1
            elif c1 < start:
                count += 1
                # c1 inherit c2, c2 got new far right
                if c2 < end:
                    c1, c2 = c2, end
                # c2 is already far right, c1 smaller by 1
                else:
                    c1 = c2 - 1
            # or c1, c2 are both inside, preserve current choices
        return count