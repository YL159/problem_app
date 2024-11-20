'''
Leetcode 2246. Longest Path With Different Adjacent Characters
Given an array of parents, parent[i] is parent of node i,
and string of the same length as # of nodes, s[i] is node i's char.
Find the max lenght of a path that adjacent nodes have different chars.

Since we only care about adjacent chars are different <=> only consider parent - child scope
Thus use post order traversal and incremental methods to recursively collect constructable info:
	local optimal, optimal with loose end (for future optimal)
=>	return (subtree's optimal path, optimal path ends with subtree root)
'''
from typing import List
import collections

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # post order traversal with incremental method
        # construct parent->children map
        tree = collections.defaultdict(list)
        for i, p in enumerate(parent):
            if p == -1:
                continue
            tree[p].append(i)
        
        # return longest path, longest path end with rt
        def postOrder(rt: int) -> tuple:
            if rt not in tree:
                return 1, 1
            # longest within subtree rt
            local_long = 0
            # 2 longest end with child, greedy
            end_long = [0, 0]
            # longest path end with rt
            end = 1
            for c in tree[rt]:
                p, end_p = postOrder(c)
                # p >= end_p guarantee
                local_long = max(local_long, p)
                if s[rt] == s[c]:
                    continue
                if end_p >= end_long[0]:
                    end_long[0], end_long[1] = end_p, end_long[0]
                elif end_p > end_long[1]:
                    end_long[1] = end_p
                end = max(end, end_p + 1)
            local_long = max(local_long, sum(end_long) + 1)
            return local_long, end
        
        return max(postOrder(0))