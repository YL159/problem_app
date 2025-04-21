'''
Leetcode 2962. Count Subarrays Where Max Element Appears at Least K Times
Max element is global max. k > 0

Find the max element's idx array, then fix window on idx array and count left/right positions

Time O(n), Space O(n)
'''
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # get the idx list of max num, e.g. [3,5,6,9...]
        m, idxs = 0, []
        for i, n in enumerate(nums):
            if n > m:
                m = n
                idxs = [i]
            elif n == m:
                idxs.append(i)
        if len(idxs) < k:
            return 0
        # subarr starts with 1,2,3; 4,5; 6; 7,8,9; ... and contain >= k max
        start, res = -1, 0
        for i in range(len(idxs)-k+1):
            res += (idxs[i] - start) * (len(nums) - idxs[i+k-1])
            start = idxs[i]
        return res