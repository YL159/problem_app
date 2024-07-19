'''
Leetcode 2477. Minimum Fuel Cost to Report to the Capital
Every node has 1 person and 1 car to go to capital 0. Each car has maximum seats. 1 car move 1 edge cost 1 fuel
Find the min fuel cost for every person to report to the capital

Construct adjacency map of the tree. Children points to parent is fine.
For each subtree, use post-order recursively get # of people and # of cars from each child node.
Thus for subtree root node, all these cars spends 1 fuel each to reach root. And redistribute people to min # of cars
'''
from typing import List
import collections, math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # construct tree from roads
        self.book = collections.defaultdict(list)
        self.seats = seats
        self.cost = 0
        for a, b in roads:
            self.book[a].append(b)
            self.book[b].append(a)

        # post-order traversal, hint parent node to avoid
        self.postOrder(0, -1)
        return self.cost

    def postOrder(self, rt: int, parent: int) -> tuple:
        # return subtree (# of ppl, # of cars)
        if not self.book[rt]:
            return 1, 1
        ppl = 1
        for n in self.book[rt]:
            if n == parent:
                continue
            p, car = self.postOrder(n, rt)
            self.cost += car
            ppl += p
        cars = math.ceil(ppl / self.seats)
        return ppl, cars