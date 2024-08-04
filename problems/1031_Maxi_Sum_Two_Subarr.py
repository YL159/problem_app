'''
Leetcode 1031. Maximum Sum of Two Non-Overlapping Subarrays
Given a number list and 2 segment length, find the max sum of 2 non-overlapping subarrays of the num list,
each of given length.

Use prefix sum to get the candidate subarray sums of 2 lengths.
Loop on 1 length, find the max sum of the other length's subarrays, and update global max.
The max sum of the other length's subarrays can be precalculated by prefix/suffix max on its candidate array.
'''
from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # overall time O(n) and space O(n)
        # create prefix sum starting at 0
        pref = [0]
        s = 0
        for n in nums:
            s += n
            pref.append(s)
        # prefix sum array of firstLen & secondLen blocks
        first = [pref[i] - pref[i-firstLen] for i in range(firstLen, len(pref))]
        sec = [pref[i] - pref[i-secondLen] for i in range(secondLen, len(pref))]
        # anchor on firstLen segments, make prefix/suffix max array of secondLen
        # memo array to find max sum of remaining secondLen blocks.
        sec_m, sec_m_rev = [], []
        m1, m2 = 0, 0
        for i in range(len(sec)):
            m1, m2 = max(m1, sec[i]), max(m2, sec[len(sec)-i-1])
            sec_m.append(m1)
            sec_m_rev.append(m2)
        sec_m_rev.reverse()
        # find the global max sum of valid firstLen/secondLen blocks
        res = 0
        for i, f in enumerate(first):
            l, r = 0, 0
            if i >= secondLen:
                l = sec_m[i-secondLen]
            if i < len(nums) - firstLen - secondLen:
                r = sec_m_rev[i + firstLen]
            res = max(res, f + max(l, r))
        return res
