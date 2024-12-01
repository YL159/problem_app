'''
Leetcode 947. Most Stones Removed with Same Row or Column
Given series of stone coordinates, you can remove a stone that has other stone with same x or y
Find max # of stones to remove

We can treat points as nodes in a graph, that connect each other if they have same x or y
Within a connected group of nodes, use strategy:
	remove the least connected nodes (min in-degree)
    then gradually to the most connected, till 1 node left
Thus each group left 1 node, while removing the most of the nodes
'''
from typing import List
import collections

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # aggregate points by x and y
        X = collections.defaultdict(set)
        Y = collections.defaultdict(set)
        for a, b in stones:
            X[a].add((a, b))
            Y[b].add((a, b))
        
        res = 0
        visited_x = set()
        visited = set()
        # BFS iteratively find new xs in a group, using y as bridge
        for x in X:
            if x in visited_x:
                continue
            group = 0
            visited_x.add(x)
            cur, nex = X[x], set()
            while cur:
                group += len(cur)
                visited |= cur
                for _, y1 in cur:
                    for x1, _ in Y[y1] - visited:
                        visited_x.add(x1)
                        nex |= X[x1]
                cur, nex = nex, set()
            res += group - 1
        return res