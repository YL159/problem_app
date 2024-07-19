'''
Leetcode 1443. Minimum Time to Collect All Apples in a Tree
Given a list of edges of a tree, and bool list of apple sites of tree nodes
Find the min time of a round trip from 0 to collect all apples. 1 edge count 1 time unit

Construct adjacency map of the tree, use DFS with path back track to traverse each node.
For each subtree:
	Accept each edge to root's children
	Validate or reject above decision according to recursive DFS result
	If any of its subtrees has apple, return True
'''

from typing import List
import collections

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # adjacency map
        self.graph = collections.defaultdict(list)
        self.apples = hasApple
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.t = 0
        self.dfs(0, 0)
        return self.t

    # DFS backtrack check if each path has apples or not
    def dfs(self, parent: int, x: int) -> bool:
        got_apple = False
        for i in self.graph[x]:
            if i == parent:
                continue
            # default include edge x->i
            self.t += 1
            sub = self.dfs(x, i)
            # if subtree i has apples, validate i->x back edge by +1
            # or no apples in subtree i, exclude back edge by -1
            self.t += 1 if sub else -1
            got_apple |= sub
        # return true if this subtree x has any apples
        if got_apple or self.apples[x]:
            return True
        return False
        