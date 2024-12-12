'''
Leetcode 2467. Most Profitable Path in a Tree
A tree has 0~n-1 labeled nodes. Each node of a tree has a value amount[i].
Alice starts at root 0 traveling to some leaf, and Bob starts at some node traveling to root 0.
They start at the same time, travel 1 edge at a time towards their own target node.
	If they meet, Alice got half of the amount.
	If Alice visited a node that Bob already visited, got 0 profit/payment
	otherwise Alice get full profit/payment
Find Alice's max profit.

Bob's profit is of no concern, and his path is fixed. Pre-calculate his path with time stamp.
For Alice, check each of her path while considering Bob's path effect on each node.
Then find global max.
'''
from typing import List
import collections

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # mark bob's path with time stamp
        # dfs on alice's every path, account for bob's path effect. find max
        self.tree = collections.defaultdict(list)
        for a, b in edges:
            self.tree[a].append(b)
            self.tree[b].append(a)
        
        # backtrack check & mark bob's path
        self.bob = bob
        bobs = []
        self.findBob(0, -1, bobs)
        self.book = {x: len(bobs)-i-1 for i, x in enumerate(bobs)}

        # dfs on alice paths
        self.amount = amount
        self.res = float('-inf')
        self.findAlice(0, -1, 0, 0)
        return self.res

    # backtrack check & mark bob's path
    def findBob(self, cur: int, parent: int, path: list) -> bool:
        path.append(cur)
        if cur == self.bob:
            return True
        for nex in self.tree[cur]:
            if nex == parent:
                continue
            if self.findBob(nex, cur, path):
                return True
        path.pop()
        return False
    
    # dfs for each alice's path, cope with bob's path & time
    def findAlice(self, cur: int, parent: int, t: int, profit: int) -> None:
        if cur not in self.book or t < self.book[cur]:
            cur_profit = self.amount[cur]
        elif t == self.book[cur]:
            cur_profit = self.amount[cur] // 2
        else:
            cur_profit = 0
        pft = profit + cur_profit
        if len(self.tree[cur]) == 1 and self.tree[cur][0] == parent:
            self.res = max(self.res, pft)
            return
        for nex in self.tree[cur]:
            if nex == parent:
                continue
            self.findAlice(nex, cur, t+1, pft)
        