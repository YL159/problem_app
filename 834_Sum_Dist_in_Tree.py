'''
Leetcode 834. Sum of Distances in Tree
Given an array of edges, return each node's total edge distance to all other nodes

Post order traversal only get the result of current root. And repeat this for every node.
Thus a bi-directional adjacency map is needed, in order to get a subtree result from every perspective, i.e. from every neighbor
And thus use DP in post order to reuse previous result if looking for a subtree result from the same perspective.
'''
from typing import List
import collections

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.tree = collections.defaultdict(dict)
        # construct a memo dict. tree[parent][child] is from parent -> child perspective, with value:
        # (total dist if include child subtree, total # of nodes in child subtree)
        for a, b in edges:
            self.tree[a][b] = None
            self.tree[b][a] = None
        res = [0] * n
        # -1 node as parent of all nodes, to simulate each node as tree root.
        for i in range(n):
            self.postOrder(-1, i)
            res[i] = self.tree[-1][i][0]
        return res
    
    # return (total dist to rt, total # of nodes in subtree rt) and update tree
    def postOrder(self, pt: int, rt: int) -> tuple:
        # if tree[-1][rt] is already calculated, tree[rt][pt] must also be calculated
        # use it to get tree[pt][rt] result
        if rt in self.tree[-1]:
            total_rt, count = self.tree[-1][rt]
            dist, cnt = self.tree[rt][pt]
            d, c = total_rt - dist - cnt, count - cnt
            self.tree[pt][rt] = (d, c)
            return d, c
        # else recursively calculate rt's children, but use existing results if any
        d, c = 0, 1
        for k in self.tree[rt]:
            if k == pt:
                continue
            dist, cnt = 0, 0
            if self.tree[rt][k]:
                dist, cnt = self.tree[rt][k]
            else:
                dist, cnt = self.postOrder(rt, k)
            d += dist + cnt
            c += cnt
        self.tree[pt][rt] = (d, c)
        return d, c
