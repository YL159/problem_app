'''
Leetcode 1519. Number of Nodes in the Sub-Tree With the Same Label
Given edges of unique-node-number tree, and labels for each node number, find the # of same label nodes as root in each subtree

Use post order traversal to count label appearances
# of the same label as subtree root = label count after post order on root - label count before
'''
from typing import List
import collections

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.labels = labels
        self.tree = collections.defaultdict(list)
        for a, b in edges:
            self.tree[a].append(b)
            self.tree[b].append(a)
        self.res = [0] * n
        # char: int count # of char seen so far
        self.count = collections.defaultdict(int)
        # add -1 to root to avoid been regarded as leaf
        self.tree[0].append(-1)
        self.postOrder(0, -1)
        return self.res
    
    def postOrder(self, rt: int, parent: int) -> None:
        c = self.labels[rt]
        prev = self.count[c]
        self.count[c] += 1
        for node in self.tree[rt]:
            if node == parent:
                continue
            self.postOrder(node, rt)
        # rt label appearance in subtree = label # difference before/after visit
        self.res[rt] = self.count[c] - prev
        return
        