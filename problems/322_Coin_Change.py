'''
Leetcode 322. Coin Change
Given an array of coin denominations, find the least # of coins that sum up to given amount

DP on every amount [0, amount], build from smaller amount to larger amount. If not possible, denote -1.
For every coin, check if there is optimum solution for (current amount - coin). Current opt is +1 on that.
And find the min(opt of current amount from all coins source)
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # check larger coin to later populate dp with smaller i
        coins.sort(reverse=True)
        dp = [0] * (amount+1)
        # alternative of infinity
        big = amount // coins[-1] + 1
        for i in range(1, amount+1):
            opt = big
            # check if any optimum result for i-c
            for c in coins:
                if i < c or dp[i-c] < 0:
                    continue
                opt = min(opt, dp[i-c]+1)
            if opt == big:
                dp[i] = -1
            else:
                dp[i] = opt
        return dp[-1]