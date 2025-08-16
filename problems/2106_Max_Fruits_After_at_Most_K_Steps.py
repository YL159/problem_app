'''
Leetcode 2106. Maximum Fruits Harvested After at Most K Steps
Given a sorted list of [position, amount] fruit info, and start position. In each step:
	move to left or right 1-unit
Take all fruits at current position if any
Find the max amount of fruits to take after at most k steps.

Even though we can go anywhere anytime, we want to reduce the steps that repeats on visited positions.
	=> Greedily go to very left and go right, or go to very right and go left within k steps
thus each position is visited at most twice
Edge cases are going one way to very left or very right and no going back.
Use prefix sum and binary search to identify the left/right max reach before going right/left.
Time O(nlogn), Space O(n)

Potentially time O(n), if using 2-pointers to find left/right max reach.
'''

import bisect
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # turn back at most once
        right_start = bisect.bisect(fruits, [startPos, float('inf')])
        # build prefix sum of left portion backwards
        left_pref = [(0, 0)]
        for i in range(right_start - 1, -1, -1):
            pos, amount = fruits[i]
            if startPos-pos > k:
                break
            left_pref.append((startPos-pos, left_pref[-1][1]+amount))
        
        left_idx = bisect.bisect(left_pref, (k, float('inf'))) - 1
        res = left_pref[left_idx][1]
        if right_start == len(fruits):
            return res

        right_res = 0
        for i in range(right_start, len(fruits)):
            pos, amount = fruits[i]
            right_res += amount
            cur_res, left_res = 0, 0
            # if reaching each right fruit, check BEFOREHAND how far left can be reached
            # also reaching each right fruit, check THEN how far left to reach
            distances = [(k+startPos-pos)//2, k-(pos-startPos)*2]
            if all(d < 0 for d in distances):
                break

            for left_dist in distances:
                if left_dist >= 0:
                    left_idx = bisect.bisect(left_pref, (left_dist, float('inf'))) - 1
                    left_res = left_pref[left_idx][1]
                cur_res = max(cur_res, left_res + right_res)
            
            res = max(res, cur_res)
        return res