'''
Leetcode 1376. Time Needed to Inform All Employees
n employees forming a tree of employment. Each one has only 1 manager, and specific informTime to propagate.
Find the time that all employees are informed of a message.

Construct a directional tree map. Use DFS and prefix sum along a path of propagation to find the max time among all paths.
'''
from typing import List
import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # find the longest time of a path
        self.tree = collections.defaultdict(list)
        for i, n in enumerate(manager):
            if i == headID:
                continue
            self.tree[n].append(i)
        self.res = 0
        self.it = informTime
        self.dfs(headID, 0)
        return self.res
    
    # use prefix sum s instead of sum(path infotime)
    def dfs(self, rt: int, s: int) -> None:
        if rt not in self.tree:
            self.res = max(self.res, s)
            return
        t = s + self.it[rt]
        for n in self.tree[rt]:
            self.dfs(n, t)