'''
Leetcode 518. Coin Change II
Given target amount and a list of coin values, determine # of coin combinations that sum to amount.

DP on calculated coins and their possible sums.
for coin c:
	combinations of sum s = s with visited coins + s with at least 1x c
Build all possible sums from 1 coin values to all values.

Best solution is 3rd. Use the same DP array.
For each new coin(say 2), adding 1x 2 from whatever previous solutions (even a combination contains some 2s)
will form a new solution.
'''
from typing import List
import collections

# 1st. dictionary approach, ~ 1600ms
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        # all possible sum with current subset of coins
        book = collections.defaultdict(int)
        for coin in coins:
            if coin > amount:
                break
            # all possible sum including >= 1x current coin
            book1 = collections.defaultdict(int)
            for mult in range(coin, amount+1, coin):
                book1[mult] += 1
                for k, v in book.items():
                    if k + mult <= amount:
                        book1[k + mult] += v
            # merge to main book
            for k, v in book1.items():
                book[k] += v
        return book[amount]

# 2nd. a list version of similar approach. ~ 1900ms takes more time. Time O(c*amount*amount/coin)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cur, nex = [0] * (amount+1), [0] * (amount+1)
        for coin in coins:
            cur[0] = 1
            for i in range(min(len(cur), coin)):
                nex[i] = cur[i]
            for i in range(coin, amount+1):
                j = i
                while j >= 0:
                    nex[i] += cur[j]
                    j -= coin
            cur, nex = nex, [0] * (amount+1)
        return cur[amount]

# 3rd approach, upgrade from 2nd. use nex and cur to construct nex
# this idea is really close to 4th. ~ 100ms, Time O(c*amount), Space O(c*amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cur, nex = [0] * (amount+1), [0] * (amount+1)
        cur[0] = 1
        for coin in coins:
            for i in range(min(len(cur), coin)):
                nex[i] = cur[i]
            for i in range(coin, amount+1):
                nex[i] = cur[i] + nex[i-coin]
            cur, nex = nex, [0] * (amount+1)
        return cur[amount]
    
# 4th best approach, same DP array use. ~ 100ms Time O(c*amount), Space O(amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]