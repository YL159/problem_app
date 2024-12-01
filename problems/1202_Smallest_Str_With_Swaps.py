'''
leetcode 1202. Smallest String With Swaps
Given a string, and a list of swappable pairs of idx. Can swap between the idx pairs any # of times.
Find the lexicographically smallest string after swap.

Basically, if we have pair [0, 3], [3, 2], [2, 6], we can swap [0, 2, 3, 6] letters for any target sequence.
Thus the problem is:
	Find the swappable groups (connected idx groups) of letters, rearrange for smallest seq within a group
	Then combine all idx from different groups to result str

Use BFS and union find for the connected groups.
'''
from typing import List
import collections

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # find connected groups of the idx pairs, then smallest arrangement within groups
        book = collections.defaultdict(set)
        for a, b in pairs:
            book[a].add(b)
            book[b].add(a)

        visited = set()
        groups = []
        for i in range(len(s)):
            if i in visited:
                continue
            groups.append(set())
            cur, nex = {i}, set()
            # bfs union find a connected group
            while cur:
                groups[-1].update(cur)
                visited.update(cur)
                for x in cur:
                    nex |= book[x] - visited
                cur, nex = nex, set()
        
        res = [None] * len(s)
        for g in groups:
            mapping = zip(sorted(g), sorted(s[idx] for idx in g))
            for i, c in mapping:
                res[i] = c
        return ''.join(res)
