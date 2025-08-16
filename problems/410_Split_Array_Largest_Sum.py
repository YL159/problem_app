'''
Leetcode 410. Split Array Largest Sum
Given an array of positive ints, split it into k non-empty subarrs.
Find the min of max subarr sum of a split config.

Directly split array into exactly k subarrs gives huge decision tree.

Method 1, DP build k split from best results of k-1 splits. Similar to #813

Time O(kn^2), Space O(kn)

Method 2, binary search for such max subarr sum.
Subarr sum is limited in range min(nums) ~ sum(nums).
If we fix the max subarr sum as t, it is easy to check if nums can be split into exactly k subarrs:
	=> for each subarr, greedily consume nums if smaller than t
		check if split is <= k
	=> if < k, split some subarr into even smaller subarrs to meet k split because k <= len(nums)
	=> if > k, impossible max subarr sum, too small, should increase it
Thus the subarr sum range can be partitioned into possible ~ impossible 2 sections
	=> binary search for this min subarr sum that makes it possible
Time O(nlog(sum(nums))), Space O(1)
'''

from typing import List

class Solution:
	# Method 1, similar to #813
	# build DP on best result for splitting nums[:i] into x subarrs
	# for new nums[i], best result of split into x comes from best of:
	# nums[:j] split into x-1 subarr for j in i-1...x
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        if k == 1:
            return sum(nums)
        n = len(nums)
        dp = [[0] * n for _ in range(k+1)]
        # build base case k=1
        pref = 0
        for i in range(n):
            pref += nums[i]
            dp[1][i] = pref
        
		# split nums[,i] into x subarrs
		# dp[x][i] = best(dp[x-1][x-1...i-1])
        for x in range(2, k+1):
			# when x=k, we need only dp[k][-1], thus skip dp[k][,n-2] calculation
            low = x-1 if x != k else n-1
            for i in range(low, n):
                tail = 0
                opt = float('inf')
                for j in range(i, x-2, -1):
                    tail += nums[j]
                    opt = min(opt, max(dp[x-1][j-1], tail))
                dp[x][i] = opt
        return dp[k][-1]
