'''
Leetcode 518. Coin Change II
Given target amount and a list of coin values, determine # of coin combinations that sum to amount.

DP on calculated coins and their possible sums.
for coin c:
	combinations of sum s = s with visited coins + s with at least 1x c
Build all possible sums from 1 coin values to all values.
'''
from typing import List
import collections

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