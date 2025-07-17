'''
Leetcode 3202. Find the Maximum Length of Valid Subsequence II
Given an int array and positive int k, find the longest subseq that:
	Sums of neighbor subseq items % k are the same.

Since we care only the remainder after mod k, and (sub[i] + sub[i+1]) % k = (sub[i]%k + sub[i+1]%k) % k
Thus transfore each number in arr into mod k remainder.

Use incremental idea, for each rem in arr, what is the longest previous sequence it can append to?
	=> isolate target remainder value v of range(k)
    	for each target remainder, there is a counter part remainder to match:
        e.g. rem(sub[i]) = 1, k = 4, consider target remainder 3, thus to find the latest visited rem(sub[j]) = x that
				(1 + x) % 4 = 3 => x = (3 - 1) % 4 = 2, (0 <= x < 4)
        if we visited a number with remainder 2, find the latest appearance and append current number to it
    => +1 to the length of latest appeared "other remainder" at target value v
Finding the latest appearance guarantees the longest previous subseq, because it is non-decreasing.

Use 2D-DP of len(nums) * k size, populate each row by finding its matching other remainder and add 1 to its length
Result is the max number in the matrix.

Time O(nk), Space O(nk)
'''

import collections
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 2d-dp of each nums[i] vs target value v = (sub[0]+sub[1])%k
        dp = [[0]*k for _ in range(len(nums))]
        # record the last idx of nums[i]%k
        pos = collections.defaultdict(int)
        res = 0
        for i, n in enumerate(nums):
            rem = n%k
            for v in range(k):
                # the other sub[?] remainder matching rem to get target v
                rem2 = (v-rem)%k
                tmp = 1
                # if visited rem2, current n can append to rem2's longest subseq
                if rem2 in pos:
                    tmp = dp[pos[rem2]][v] + 1
                dp[i][v] = tmp
                res = max(res, tmp)
            pos[rem] = i
        return res