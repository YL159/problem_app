'''
Leetcode 309. Best Time to Buy and Sell Stock with Cooldown
Given an array of stock price, find max profix.
Only buy stock without holding one, and after 1-day cooldown of last sell.

Here use 4 states for every day: buy a stock, wait after a bought, wait after a sell, sell a stock
They store the current optimum result of that day.
Make the state transition rules for every day:

Buy comes from prev wait_sell, meaning cooldown at least 1 day
Wait_buy comes from max of prev buy and wait_buy
Wait_sell comes from max of prev wait_sell and sell
Sell comes from max of prev buy and wait_buy

3 states are also workable. buy & wait after buy can be merged.
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        # best result for states of every day: [buy, wait after buy, wait after sell, sell]
        buy, wait_buy, wait_sell, sell = -prices[0], float('-inf'), 0, 0
        for n in prices[1:]:
            # today's opt buy: opt of some wait after prev sell - today price
            buy1 = wait_sell - n
            # today's opt wait after buy:  yesterday's max(buy, wait after buy)
            wait_buy1 = max(buy, wait_buy)
            # today's opt wait after sell: yesterday's max(wait after sell, just sell)
            wait_sell1 = max(wait_sell, sell)
            # today's opt sell: yesterday's max(buy, wait after buy) + today price
            sell1 = max(buy, wait_buy) + n
            buy, wait_buy, wait_sell, sell = buy1, wait_buy1, wait_sell1, sell1
        return max(wait_sell, sell)