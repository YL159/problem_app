'''
Leetcode 3578_Count_Partitions_With_Max-Min_Diff_at_Most K
Give an int array nums, and min-max diff k >= 0
Find how many partions of nums so that each subarr's min-max diff <= k

Observations:
Partition problems usually use target binary search, incremental dp.
Here use incremental DP.
And the corresponding left limit for subarr ending at index i, always increases as i increases.

DP[i] = count of valid partions of subarr nums[0, i]. Result is DP[-1]
For each new #, check how far to the left the subarr ending at this # can reach
and reuse results on the way to the left limit
    => Time complexity O(n^2) checking left limit for each ending idx
    => Space complexity O(n) keeping DP array for reuse

Problem is finding min-max for each subarr ending at index i.
Min-max for nums[0, i] is easy, but if their diff > k, need to find next min or max
    => use monotonic que to find next min-max if cur min-max diff > k
    => pop left of min max monotonic que untill their diff <= k
    => update left limit for current subarr ending at i according to any popped indices

Since we need sum(DP[left_limit, i]), use DP prefix sum array instead.

Time O(n) each item enter-exit a que max once. Space O(n)
'''

from typing import List

import collections

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        # DP array is hidden, and represented by its prefix sum array
        dp_pref = [0, 1]
        # monotonic min-max queue holding the candidates of min-max on the way
        maxq = collections.deque()
        minq = collections.deque()
        maxq.append(0)
        minq.append(0)
        # left limit for each ending index, monotonically increasing
        left = 0
        for i in range(1, len(nums)):
            n = nums[i]
            # maintain min-max queue
            while maxq and n > nums[maxq[-1]]:
                maxq.pop()
            maxq.append(i)
            while minq and n < nums[minq[-1]]:
                minq.pop()
            minq.append(i)
            # pop left-most invalid min or max, untill their diff <= k
            # update left limit with next of popped index if possible
            if nums[maxq[0]] - nums[minq[0]] > k:
                while nums[maxq[0]] - nums[minq[0]] > k:
                    if minq[0] < maxq[0]:
                        left = max(left, minq.popleft() + 1)
                    else:
                        left = max(left, maxq.popleft() + 1)
            # current DP[i] = sum(DP[left, i-1]) = dp_pref[-1] - dp[left-1]
            # thus dp_pref[i] = dp_pref[-1] + DP[i] = dp_pref[-1] * 2 - dp[left-1]
            dp_pref.append((dp_pref[-1] * 2 - dp_pref[max(left-1, 0)] + (left==0)) % mod)
        return (dp_pref[-1] - dp_pref[-2]) % mod