'''
Leetcode 2385. Amount of Time for Binary Tree to Be Infected
From an infected node of a tree with unique node values, 1 unit time an infected node infects neighboring clean nodes.
Find the time all nodes are infected.

Treat the tree as an undirected graph, start with the infected node and BFS check the max depth from all sides.
Instead of converting into undirected graph, which may introduce 'visited' node check,
1. BFS make a directed adjacency map of the tree. It is rooted at root node
2. DFS find the path from root to start node, make each edge in the path reversed in the map to root from start node.
3. BFS check the max depth from start node.
'''
from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # BFS make a directed graph from root
        graph = collections.defaultdict(list)
        cur = [root]
        while cur:
            nex = []
            for node in cur:
                if node.left:
                    nex.append(node.left)
                    graph[node.val].append(node.left.val)
                if node.right:
                    nex.append(node.right)
                    graph[node.val].append(node.right.val)
            cur = nex
        # find the path from root to start
        self.path = [root.val]
        self.start = start
        self.dfsPath(root)
        # reverse the path edges in directed graph
        for i in range(len(self.path)-1):
            a, b = self.path[i:i+2]
            graph[a].remove(b)
            graph[b].append(a)

        # now the directed graph is rooted at start. BFS check for max depth
        count = 0
        cur = [start]
        while cur:
            nex = []
            count += 1
            for n in cur:
                nex.extend(graph[n])
            cur = nex
        return count - 1

    def dfsPath(self, rt: Optional[TreeNode]) -> bool:
        if rt.val == self.start:
            return True
        if rt.left:
            self.path.append(rt.left.val)
            if self.dfsPath(rt.left):
                return True
            self.path.pop()
        if rt.right:
            self.path.append(rt.right.val)
            if self.dfsPath(rt.right):
                return True
            self.path.pop()
        return False