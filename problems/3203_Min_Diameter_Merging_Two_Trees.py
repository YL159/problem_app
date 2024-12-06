'''
Leetcode 3203. Find Minimum Diameter After Merging Two Trees
Given 2 list of edges of 2 trees, merging them to create 1 tree.
Of all merged trees, find the min length of their longest path.

We want to connect 2 trees at "middle node", i.e. select a root of a tree at the middle of its longest path.
So that even connected, the longest path of result tree is minimized.
As hint says, another candidate is the longest path of each tree, they can also be the global longest.
Thus for each tree, we calculate the 'half' of longest path, and the longest path itself

To get the longest path, hint by #310, we can iteratively prune the leaf nodes.
The nodes in the center of longest path must be the last to be pruned. Record # of iteration

Time O(m+n) since we visit each node of each tree twice, building adjacency set + pruning each node
Space O(m+n)
'''
from typing import List
import collections

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # concat min of longest path in both trees
        # 1 tree may have the global longest, need to compare
        semi1, l1 = self.minLong(edges1)
        semi2, l2 = self.minLong(edges2)
        return  max(semi1 + semi2 + 1, l1, l2)
    
    def minLong(self, edges: List[List[int]]) -> tuple:
        tree = collections.defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        
        leaves = set()
        for k, v in tree.items():
            if len(v) == 1:
                leaves.add(k)
		# trim leaves till 1-2 nodes left
        count = 0
        while len(leaves) >= 2:
            count += 1
            nex = set()
            for lea in leaves:
                if not tree[lea]:
                    break
                p = tree[lea].pop()
                tree[p].remove(lea)
                if len(tree[p]) == 1:
                    nex.add(p)
            leaves = nex
        # remain 1 leaf => center of longest path is the node, length = count * 2
        # remain no leaf => center of longest path is an edge, counted twice, length = count * 2 - 1
        return (count, count * 2 - (len(leaves) == 0))
            
