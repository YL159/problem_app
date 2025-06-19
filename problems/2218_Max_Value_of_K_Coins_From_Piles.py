'''
Leetcode 2218. Maximum Value of K Coins From Piles
Given n piles of coins with positive values, take k coins from these piles like stacks.
Find the max total value of these k coins.

Reduce search space by limiting first p+1 piles picking t coins
	=> build dp[p][t] as optimum result for: max value of take t coins in total from piles[0,p]
And work from dp[0][0] to dp[0][k] to dp[piles][k]

dp[p][t] comes from max of:
	0 coins from piles[p] AND max value of t coins from piles[0,p-1]
		=> 0 + dp[p-1][t]
	1 coin from piles[p] AND max value of t-1 coins from piles[0,p-1]
		=> sum(piles[p][:1]) + dp[p-1][t-1]
    ...
    all coins from piles[p] AND max value of t-all coins from piles[0,p-1]
		=> sum(piles[p]) + dp[p-1][t-len(piles[p])]

thus dp[p][t] = max( dp[p-1][t-i] + sum(piles[p][0,i] for i in range(t)) )

Since dp[p] row depends only dp[p-1] row, use dp array iteration for better memory management
And use piles[p] prefix sum for quick access sum(piles[p][0,i])
Time O(nk*max(pile_len)), Space O(k)
'''
from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # make prefix sum of each pile for easier top sums
        for pile in piles:
            for i in range(1, len(pile)):
                pile[i] += pile[i-1]
            # prefix sum 0 at the end to commodate pile[-1] access later
            pile.append(0)
        
        dp, nex = [0]*(k+1), [0]*(k+1)
        for t in range(min(k+1, len(piles[0]))):
            dp[t] = piles[0][t-1]
        for p in range(1, len(piles)):
            for total in range(k+1):
                # find opt of taking up to 'total' coins from piles[p]
                # piles[p] length already increased by 1
                for take in range(min(total+1, len(piles[p]))):
                    nex[total] = max(dp[total-take] + piles[p][take-1], nex[total])
            dp, nex = nex, [0]*(k+1)
        return dp[-1]
            
