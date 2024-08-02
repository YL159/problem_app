'''
Leetcode 851. Loud and Rich
Given a list of richer-than tuples, and people's quietness, find the quietest ppl no poorer than each person.

Construct a dictionary of {ppl: list of directly richer ppl}
To avoid re-evaluation of ppl who are not the poorest:
Use recursive topological traversal, evaluate richest ppl first and ripple to poorest.
Use DP and memorize evaluated ppl.
'''
from typing import List 

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        q_book = {q: i for i, q in enumerate(quiet)}

        rich_neighbor = {i:[] for i in range(n)}
        for r, p in richer:
            rich_neighbor[p].append(r)
        
        q_res = {}
        
        # DP and topologically find result from richest to poorest
        def solve(p: int) -> int:
            # already solved p, return result
            if p in q_res:
                return q_res[p]
            # not solved, but also got nobody richer, return p's quietness
            q = quiet[p]
            if not rich_neighbor[p]:
                q_res[p] = q
                return q
            # got some richer neighbors, get their quietness and min
            for ppl in rich_neighbor[p]:
                q = min(q, solve(ppl))
            q_res[p] = q
            return q
            
        for i in range(n):
            solve(i)
        return [q_book[q_res[p]] for p in range(n)]
