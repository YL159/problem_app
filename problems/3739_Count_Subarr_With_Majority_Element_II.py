'''
Leetcode 3739. Count Subarrays With Majority Element II
Given a nums array, and target int
Find count of all subarrs with target as major:
    has # == target count strictly more than half of subarr length

Observation:
e.g. nums = [1, 2, 2, 2, 3, 4, 2, 2], target = 2
1. each # either equal to target or not
    => transform into [0, 1, 1, 1, 0, 0, 1, 1]
2. each 0 cancels previous 1's contribution in subarr
    => transform into [-1, 1, 1, 1, -1, -1, 1, 1]
3. subarr problem can make use of prefix sum, since each # has equal weight
    => transform [0, -1, 0, 1, 2, 1, 0, 1, 2]

Now for each ending right #, we want to know how many legitimate left start.
Target as major => count all such pref[l] < pref[cur r]

Normally, if pref[r] is unpredictable, the counting of pref[l] will be O(n) time
But importantly, current pref[r] is predictably increases by -1 or 1
    => legitimate max pref[l] is also moving left or right by 1
    => prefsum of pref[l] < pref[r] can then be easily maintained

Time O(n), Space O(n)
'''

from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref = [0]
        p = 0
        # get the prefix sum of transformed -1/1 nums array
        for n in nums:
            v = 1 if n == target else -1
            pref.append(pref[-1] + v)
        
        res = 0
        record = {0: 1} # record[i]: the count of pref == i
        psmall = pref[1]-2 # initially psmall is either -3 or -1
        psum = record.get(psmall, 0)
        for p in pref[1:]:
            # maintain psum, sum of count of smaller prefix
            # p only increase by -1/1, thus p - psmall is now either 2/0
            # update psum, and then psmall always 1 smaller than p
            if p - psmall == 2:
                psmall += 1
                psum += record.get(psmall, 0)
            else:
                psum -= record.get(psmall, 0)
                psmall -= 1
            
            res += psum
            # late update p record without interrupting psum calculation
            record[p] = record.get(p, 0) + 1
        return res

