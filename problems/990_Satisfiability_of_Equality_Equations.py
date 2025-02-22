'''
Leetcode 990. Satisfiability of Equality Equations
Given a list of strs representing equality and inequality between single-letter variables:
'a=b', 'c!=d' ...
Return True if the set of formula is consistent, otherwise False

We can process the equalities first, and then evaluate if those inequalities break any of them,
	or see any self contradictions like 'c!=c'
Equal variables can be assigned a special group name.
	=> Inequalities should observe different group names between variables
Thus use graph union find each group of equal variables.
'''
from typing import List
import collections

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # build a equality graph of letters, verify if inequality violates existing equality
        inequal = []
        graph = collections.defaultdict(set)
        for eq in equations:
            if eq[1] == '!':
                inequal.append((eq[0], eq[3]))
                continue
            a, b = eq[0], eq[3]
            graph[a].add(b)
            graph[b].add(a)
        if not inequal:
            return True
        # BFS assign nodes in connected components with group names
        letters = {}
        visited = set()
        g = 0
        for c in graph:
            if c in letters:
                continue
            cur, nex = {c}, set()
            while cur:
                visited |= cur
                for node in cur:
                    letters[node] = g
                    nex.update(graph[node] - visited)
                cur, nex = nex, set()
            g += 1
        # validate inequalities
        for a, b in inequal:
            if a == b or a in letters and b in letters and letters[a] == letters[b]:
                return False
        return True