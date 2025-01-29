'''
Leetcode 802. Find Eventual Safe States
Given an adjacency graph list, where node i points to list of nodes in graph[i].
Terminal node: no outgoing edges.
Safe node: a terminal node or all outgoing edges eventually end at some other safe node or terminal node.
Return all safe nodes in ascending order.

consider graph = [[1,2],[2,3],[5],[0],[5],[],[]]
					0	  1	   2   3   4   5  6
Start from root 0 -> [1,2] -> [2,3 | 5] -> [5 | 0]
For path 0-1-3-0, node 0 is visited twice, thus a loop
	<=> visiting a node that appeared in current path, gives a loop
    and all nodes involved in this path is thus unsafe
So we can backtrack on paths and store visited(decided) nodes in safe/unsafe sets
and early exit to avoid exhausting the same subtrees
'''
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # exhaust each path once and record safe/terminal and unsafe/loop
        safe, unsafe = set(), set()
        # path node set of current path in tree
        pset = set()
        def backtrack(rt: int) -> bool:
            if rt in safe:
                return True
            if rt in unsafe or rt in pset:
                return False
            pset.add(rt)
            for node in graph[rt]:
                if not backtrack(node):
                    unsafe.add(rt)
                    return False
            safe.add(rt)
            pset.remove(rt)
            return True

        res = []
        for i in range(len(graph)):
            if backtrack(i):
                res.append(i)
        return res