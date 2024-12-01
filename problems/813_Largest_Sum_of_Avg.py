'''
Leetcode 813. Largest Sum of Averages
Partition a given int array into maximal k subarrays, the score of a partition is sum of avg(subs)
Find the largest score of this array.

Build DP from base case: k = 1, partition nums[0,i] into 1 subarr, score is avg out of each prefix sum
For case k, best partition nums[0,i] comes from max of:
	best partition of nums[0, k-1] from case k-1, + avg(nums[k, i])
							  k								 k+1, i
							  k+1							 k+2, i
							  ...							 ...
							  i-1							 i, i
Time complexity O(kn^2), space complexity O(kn).
Considering building dp[k] needs only dp[k-1] and prefix sum array, space complexity is potentially O(n)

final dp for [5,2,3,4], k=3, prefix sum = [0,5,7,10,14]
opt:nums[0-0], 	[0-1],  [0-2],  [0-3]

k=1   	[5.0,   3.5,    3.33,   3.5]
k=2   	[0,     7.0,    7.5,    8.0]
k=3   	[0,     0,      10.0,   11.5]
'''
from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        if k == len(nums):
            return float(sum(nums))
        # make prefix sum array
        pref = [0]
        for n in nums:
            pref.append(pref[-1] + n)
        
        # make dp table of dp[k][n] for best score of k partion of nums[:n]
        dp = [[0]*len(nums) for _ in range(k+1)]
        # k = 1 is just avg from each prefix, partition nums[:n] into only 1 sub
        for j in range(len(nums)):
            dp[1][j] = pref[j+1] / (j+1)
        
        for i in range(2, k+1):
            prev, cur = dp[i-1], dp[i]
            # kth best partition of nums[:n]
            for j in range(i-1, len(nums)):
                opt = 0
                # max([nums[0,0] ~ nums[0,j-1] best partition(k-1) + avg(remaining)])
                for l in range(j):
                    opt = max(opt, prev[l] + (pref[j+1] - pref[l+1]) / (j-l))
                cur[j] = opt

        return dp[k][-1]