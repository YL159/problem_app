'''
Leetcode 2049. Count Nodes With the Highest Score
Given parent array, parent[i] is parent of i. Each node has a score, product of # of nodes in remaining trees if node i is removed.
Find the # of nodes that reaches highest score.

Use post-order DFS to collect the # of nodes in both subtrees, and thus get remaining # of upper nodes if removed i.
Update the global max tracking and counting. Then return # of nodes in current subtree.
'''
from typing import List
import collections

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # record current count of nodes scoring cur_max
        self.res = 0
        # record current max score
        self.cur_max = 0
        # create {parent:[children]} dictionary tree
        self.tree = collections.defaultdict(list)
        self.n = len(parents)
        for i, p in enumerate(parents):
            if p == -1:
                continue
            self.tree[p].append(i)
        
        self.postOrder(0)
        return self.res
    
    # post order traversal get # of nodes in left/right subtree, and # upper nodes
    # return # of nodes in subtree at rt
    # Also update global max score and counting result.
    def postOrder(self, rt: int) -> int:
        res = 1
        up = self.n - 1
        if rt not in self.tree:
            res = self.n - 1
        else:
            for x in self.tree[rt]:
                count = self.postOrder(x)
                res *= count
                up -= count
            if up != 0:
                res *= up
        if self.cur_max < res:
            self.res = 1
            self.cur_max = res
        elif self.cur_max == res:
            self.res += 1
        return self.n - up