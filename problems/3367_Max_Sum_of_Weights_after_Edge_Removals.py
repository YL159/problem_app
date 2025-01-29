'''
Leetcode 3367. Maximize Sum of Weights after Edge Removals

'''
from typing import List
import collections, bisect

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        # designate a root. for A -> B, A might/might not want the AB edge
        # thus post order for subtree B, it should offer 2 results:
        # B with less than k B->child edges subtree sum, and B with k B->child edges sum
        # for root's each subtree, keep less than k res add edge vs k res no edge, put diff into heap
        self.tree = collections.defaultdict(dict)
        for a, b, w in edges:
            self.tree[a][b] = w
            self.tree[b][a] = w
        self.k = k
        return max(self.postOrder(0, -1))
        
    # max result if select # of children < k, max result if select k. may be the same
    def postOrder(self, rt: int, p: int) -> tuple:
        # leaf node, regardless of k, got no edge sum
        rdict = self.tree[rt]
        if len(rdict) == 1 and p in rdict:
            return (0, 0)
        subs = {}
        for child in rdict:
            if child == p:
                continue
            s1, s = self.postOrder(child, rt)
            # child subtree sum for choose / not choose it (not choosing => this child opt to its max)
            subs[child] = (s1 + rdict[child], max(s1, s))
        if len(subs) < self.k:
            res = sum([max(v) for v in subs.values()])
            return (res, res)
        # if we choose all child, res = sum([s1+rdict[child]])
        # discard an edge means substitute some of them into max(s1, s)
        # thus try to discard those with min s1+rdict[child] - max(s1, s)
        compare = sorted([(a-b, a, b) for a, b in subs.values()])
        positive_idx = bisect.bisect(compare, (0, float('inf'), 0))
        start_idx = max(len(compare)-self.k+1, positive_idx)
        lessk = sum([t[2] for t in compare[:start_idx]]) + sum([t[1] for t in compare[start_idx:]])
        subsumk = sum([t[2] for t in compare[:-self.k]]) + sum([t[1] for t in compare[-self.k:]])
        return (lessk, subsumk)