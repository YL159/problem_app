'''
Leetcode 1155. Number of Dice Rolls With Target Sum
Given n dice ordered, each rolls [1...k] points. Find ways of dice rolls that sum up to target.

f(n, k, t) = sum(f(n-1, k, t-i) for i in [1...k])
Thus build DP array as result array from 1 dice to n dice for possible sums respectively.
And a prefix sum array is needed to mitigate subarray sum operation on DP array.
'''
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > n*k or target < n:
            return 0
        # Build a sum-way DP array of n-1 dice with all reachable targets
        dp = [1] * k
        # Build a prefix sum array of current DP array
        s = 0
        pref = [0]
        for i in range(k):
            s += dp[i]
            pref.append(s)
        # Build dp from 2 dice to n dice
        for dice in range(2, n+1):
            s = 0
            dp_nex, pref_nex = [], [0]
            # avoid index out of range issue
            pref.extend([pref[-1]]*k)
            # Each target for x dices is sum of:
            #   ways of (x-1) dices at target (target - [1...k])
            for t in range(dice, dice*k+1):
                ways = pref[t-dice+1] - pref[max(t-dice+1-k, 0)]
                dp_nex.append(ways)
                s += ways
                pref_nex.append(s)
            dp, pref = dp_nex, pref_nex
        
        return dp[target - n] % (10**9 + 7)