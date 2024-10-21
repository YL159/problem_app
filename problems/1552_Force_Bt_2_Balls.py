'''
Leetcode 1552. Magnetic Force Between Two Balls
Given coordinates of baskets and m balls, put all balls into some baskets:
min(ball distances) is max

Sort the basket coordinates.
It asks to partition coordinate distances into (m-1) groups, min(group sum) is max

If given a certain min distance x, we can easily check AT MOST how many balls/groups to partition
	Because if this x can make at most (m+2) groups, it can also make (m-1) groups by merging some of them
	=> x is not big enough

Thus binary search on this x in range(1, sum(distances)). Prefix sum arr helps.
	If max group count >= target group, record current x(mid), try larger mid => bring up left
	else => x is too large => bring down right
'''
from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        pref = [position[i]-position[0] for i in range(len(position))]
        part = m - 1
        # binary search the answer
        # check if partition to 'part' is possible on this mid
        l, r = 1, pref[-1]
        res = l
        while l <= r:
            mid = (l+r)//2
            group = 0
            pre, cur = 0, 1
            while cur < len(pref):
                if pref[cur] - pref[pre] >= mid:
                    group += 1
                    pre = cur
                cur += 1
            if group < part:
                r = mid-1
            else:
                res = max(res, mid)
                l = mid+1
        return res
