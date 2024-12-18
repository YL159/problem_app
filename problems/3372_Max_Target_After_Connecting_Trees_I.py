'''
Leetcode 3372. Maximize the Number of Target Nodes After Connecting Trees I
Given 2 trees represented by edge connections, nodes label 0 ~ n(m)
If to connect 2 trees, find the max # of target nodes within a result tree:
	within k edge range of every node in tree1.
For each query, reconnect these 2 trees as needed.

For each query node in tree1, the nodes within its k edge range is fixed.
To maximize the target nodes is to maximize those from tree2, within range k-1
=> In tree2, there is a global maximal # of nodes within k-1 range of each node.
=> res[i] = count(tree1[i]'s k range targets) + tree2's k-1 range max
'''
from typing import List
import collections

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # target nodes in tree1 is determined by target i
        # constant optimum choice of node in tree2 to directly connect to target i
        tree1 = self.makeTree(edges1)
        tree2 = self.makeTree(edges2)

        tree2_opt = 0
        if k == 1:
            tree2_opt = 1
        if k > 1:
            for node in tree2:
                tree2_opt = max(tree2_opt, self.findK(tree2, node, k-1))
        
        res = []
        for root in range(len(tree1)):
            tree1_opt = self.findK(tree1, root, k)
            res.append(tree1_opt + tree2_opt)
        return res
    
    def makeTree(self, edges: List[List[int]]) -> collections.defaultdict:
        tree = collections.defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        return tree
    
    # find max node count in a tree for each node within k range
    def findK(self, tr: collections.defaultdict, rt: int, k: int) -> int:
        if k == 1:
            return len(tr[rt]) + 1
        res = 0
        pre, cur, nex = set(), {rt}, set()
        while cur and k >= 0:
            res += len(cur)
            k -= 1
            if k < 0:
                break
            for p in cur:
                nex |= tr[p]
            nex -= pre
            pre, cur, nex = cur, nex, set()
        return res
