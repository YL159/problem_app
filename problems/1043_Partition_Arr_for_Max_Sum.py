'''
Leetcode 1043. Partition Array for Maximum Sum
Partition an array into contiguous subarrays with max length k, replace each subarray with its max value, get the max sum of array

Use DP[i] to remember the max result of arr[:i]. Each new result comes from the max of k calculations:
DP[i-j] + max(arr[i-j+1:i+1])*j, for j in [1...k]
'''

from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # initialize dp for first k elements
        dp = []
        for i in range(k):
            dp.append(max(arr[:i+1])*(i+1))
        
        i = k
        # for each new #, result is the max of all the (max of left j nums * j) + dp[i-j]
        while i < len(arr):
            cur_max = 0
            local_max = 0
            j = 1
            # need to loop from 1 to k direction to get local max correct
            while j <= k:
                # O(1) time progresively get local max of sub array arr[i-j+1:i+1]
                local_max = max(local_max, arr[i-j+1])
                cur_max = max(cur_max, dp[i-j] + local_max*j)
                j += 1
            dp.append(cur_max)
            i += 1
        return dp[-1]