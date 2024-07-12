'''
Leetcode 1361. Validate Binary Tree Nodes
Given n nodes and their left/right child array, check if they form 1 valid tree.

Form an adjacency map of all nodes.
If parent nodes not exactly 1 more than parent.intersect(children), invalid.
When BFS on the root, if a child is already visited or appear again in the same layer, invalid.
After BFS, # of visited nodes is less than all nodes, invalid.
'''
from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        tree = {x: [] for x in range(n)}
        children = set()
        for i, chs in enumerate(zip(leftChild, rightChild)):
            for c in chs:
                if c >= 0:
                    tree[i].append(c)
                    children.add(c)
        # check only 1 root
        root_set = set(tree.keys()) - children
        if len(root_set) != 1:
            return False
        # BFS check valid tree
        root = list(root_set)[0]
        visited = set()
        cur, nex = {root}, set()
        while cur:
            for p in cur:
                visited.add(p)
                for c in tree[p]:
                    if c in visited or c in nex:
                        return False
                    nex.add(c)
            cur, nex = nex, set()
        # check if any looping lone graph
        if len(visited) < n:
            return False
        return True