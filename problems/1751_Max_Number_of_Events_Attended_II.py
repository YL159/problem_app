'''
Leetcode 1751. Maximum Number of Events That Can Be Attended II
Similar setting as #1353, but:
	Meeting attendance is exclusive, non-overlapping.
	Each meeting yields a positive value if attended.
Find the max total value if attending max k meetings.

Since there are 2 metrics (value, k) to consider, and greedy may not work because meetings are exclusive
Consider each meeting's take <-> not_take choices
	=> prune the selection tree by memoize the best values under different smaller "state"
	=> state is "on-after meeting i, choosing x meetings, what is the best total value"
Naturally we should sort the meetings by start day, for efficiently finding the next non-overlapping meeting.
And memo table is based on (meeting i, choosing x) tuple, or 2d-DP array.

Time O(nlog(n) + n*k), Space O(n*k)
'''
import bisect
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # choose current event (or not), recursively decide remaining k-1 choices
        events.sort()
        # memo of best result from state tuple:
        # (from events[i] on, take max t events)
        memo = {}

        # return the best total value of choosing:
        # "remain" events after "end" time
        def recur(cur_idx: int, remain: int) -> int:
            if remain <= 0 or cur_idx >= len(events):
                memo[(cur_idx, remain)] = 0
                return 0
            
            if (cur_idx, remain) in memo:
                return memo[(cur_idx, remain)]
            
            # find the next event after taking this event
            _, end, value = events[cur_idx]
            nex_start = bisect.bisect(events, [end+1, 0, 0])
            take = value + recur(nex_start, remain-1)
            
            # if not taking this event, find best value from next event and on
            take_not = recur(cur_idx+1, remain)

            opt = max(take, take_not)
            memo[(cur_idx, remain)] = opt
            return opt
        
        return recur(0, k)