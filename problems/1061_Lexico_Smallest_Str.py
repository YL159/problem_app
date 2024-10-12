'''
Leetcode 1061. Lexicographically Smallest Equivalent String
Consider an edge between s1[i] -- s2[i].
Based on above graph, find given baseStr's smallest lexicographically equivalent string

Find the graph's connected components and their smallest char respectively.
Each baseStr letter, if in the graph, would then be replaced by respective smallest char.
'''
import collections

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # adjacency list
        adj = collections.defaultdict(set)
        for i in range(len(s1)):
            adj[s1[i]].add(s2[i])
            adj[s2[i]].add(s1[i])
        # find each letter's mapping to smallest char in its connected component
        mapping = {}
        for t in adj:
            if t in mapping:
                continue
            visited = {t}
            cur, nex = adj[t], set()
            # bfs find connected components
            while cur:
                visited |= cur
                for c in cur:
                    nex = nex.union(adj[c])
                nex -= visited
                cur, nex = nex, set()
            small = min(visited)
            for c in visited:
                mapping[c] = small
        # map baseStr char to itself or suggested by mapping
        res = []
        for c in baseStr:
            res.append(mapping.get(c, c))
        return ''.join(res)