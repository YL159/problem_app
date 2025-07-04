'''
Leetcode 1235. Maximum Profit in Job Scheduling
Given (start, end, profit) triples as jobs, find max profit from taking non-overlapping jobs
# same as #2008. Maximum Earnings From Taxi

Use incremental DP on the end points of all these jobs.
Max profit at end x = max(max(profit of taking 1 job ends at x + dp[right before start of this job]),
							not taking any job => dp[right before x])
Use binary search on the previous end point nearest to current start/x.
Thus 'the max profit at each end point' invariant is maintained (DP is non decreasing as end increases)

Time O(nlog(n)), space O(n)
'''
from typing import List
import collections, bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        ends = collections.defaultdict(list)
        for i, e in enumerate(endTime):
            ends[e].append((startTime[i], profit[i]))
        # no job end at time 1, padding by empty to accomodate idx binary search
        ends[1] = []
        end_points = sorted(ends)
        # DP profit on end time stamps
        dp = collections.defaultdict(int)
        dp[1] = 0
        for end in end_points:
            # find the best dp[end] from accepting 1 job ends at 'end'
            for start, pro in ends[end]:
                prev = bisect.bisect(end_points, start) - 1
                dp[end] = max(dp[end], dp[end_points[prev]] + pro)
            # max with NOT accepting any job ends at 'end'
            prev = bisect.bisect_left(end_points, end) - 1
            dp[end] = max(dp[end], dp[end_points[prev]])
        return dp[end_points[-1]]
